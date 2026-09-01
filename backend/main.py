import os
import re
from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from omnidimension import Client as OmniClient
from pydantic import BaseModel
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)



BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OMNIDIM_API_KEY = os.getenv("OMNIDIM_API_KEY")
OMNIDIM_AGENT_ID = int(os.getenv("OMNIDIM_AGENT_ID"))
MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

omni_client = OmniClient(OMNIDIM_API_KEY)


class WhatsAppRequest(BaseModel):
    customer_name: str = ""
    phone_number: str
    message: str = ""


@app.get("/")
async def root():
    return {"status": "AI Voice Agent backend is running"}


@app.get("/app")
async def frontend():
    return FileResponse(FRONTEND_DIR / "index.html")


@app.post("/omnidim-webhook")
async def omnidim_webhook(data: dict):
    print("\n========== OMNIDIMENSION WEBHOOK ==========")
    print(data)
    print("===========================================\n")
    return {"status": "received"}

class CallRequest(BaseModel):
    phone_number: str
@app.post("/send-whatsapp")
async def send_whatsapp(request: WhatsAppRequest):
    print("MID-CALL WHATSAPP TRIGGER")
    print("Customer:", request.customer_name)
    print("Raw Phone:", request.phone_number)

    # Clean phone number: remove '+', spaces, dashes, and extra characters
    clean_phone = re.sub(r"\D", "", request.phone_number)

    access_token = os.getenv("META_ACCESS_TOKEN")
    phone_number_id = os.getenv("PHONE_NUMBER_ID")

    # Meta Graph API version fixed to v21.0
    url = f"https://graph.facebook.com/v21.0/{phone_number_id}/messages"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    data = {
        "messaging_product": "whatsapp",
        "to": clean_phone,
        "type": "template",
        "template": {"name": "hello_world", "language": {"code": "en_US"}},
    }

    # Execute HTTP request
    response = requests.post(url, headers=headers, json=data)

    print("META STATUS:", response.status_code)
    print("META RESPONSE:", response.text)

    return {"success": response.ok, "meta_response": response.json()}
@app.post("/make-call")
async def make_call(request: CallRequest):

    phone_number = request.phone_number.strip()
    phone_number = re.sub(r"[^\d+]", "", phone_number)

    if len(phone_number) == 10 and phone_number.isdigit():
        phone_number = "+91" + phone_number

    if not re.fullmatch(r"\+91[6-9]\d{9}", phone_number):
        return {
            "success": False,
            "message": "Invalid Indian mobile number",
            "phone_number": phone_number
        }

    print("\n========== MAKE CALL ==========")
    print("Calling:", phone_number)
    print("Agent ID:", OMNIDIM_AGENT_ID)

    try:
        response = omni_client.call.dispatch_call(
            agent_id=OMNIDIM_AGENT_ID,
            to_number=phone_number
        )

        print("\n========== OMNIDIMENSION RESPONSE ==========")
        print(repr(response))
        print("=============================================\n")

        return {
            "success": True,
            "omnidimension_response": response
        }

    except Exception as e:

        print("\n========== OMNIDIMENSION ERROR ==========")
        print(repr(e))
        print("=========================================\n")

        return {
            "success": False,
            "error": str(e)
        }