\# 🎙️ AI Voice Call Agent



An AI-powered outbound voice calling backend built with FastAPI and OmniDimension.



The current version provides a REST API that can be tested through FastAPI Swagger UI. A user can provide a phone number through the API, and the backend dispatches an outbound call through an OmniDimension AI voice agent.



The project also contains an initial WhatsApp integration using the Meta WhatsApp Cloud API.







\## 🚀 Current Features



\* 📞 Initiate outbound AI voice calls

\* 🤖 OmniDimension AI voice agent integration

\* 📱 Accept phone numbers dynamically through the API

\* 📖 Interactive API testing through FastAPI Swagger UI

\* 💬 Meta WhatsApp Cloud API integration

\* 🔐 Environment-based API credentials

\* ⚡ FastAPI REST backend

\* 🔄 OmniDimension webhook endpoint







\## 🏗️ Current Architecture



text

&#x20;                FastAPI Swagger UI

&#x20;                        │

&#x20;                        │ POST /make-call

&#x20;                        ▼

&#x20;                ┌───────────────┐

&#x20;                │    FastAPI    │

&#x20;                │    Backend    │

&#x20;                └───────┬───────┘

&#x20;                        │

&#x20;                        │ dispatch\_call()

&#x20;                        ▼

&#x20;                ┌───────────────┐

&#x20;                │ OmniDimension │

&#x20;                │  AI Voice     │

&#x20;                │    Agent      │

&#x20;                └───────┬───────┘

&#x20;                        │

&#x20;                        ▼

&#x20;                   📞 Customer





&#x20;                FastAPI Backend

&#x20;                        │

&#x20;                        │ POST /send-whatsapp

&#x20;                        ▼

&#x20;                ┌───────────────┐

&#x20;                │ Meta WhatsApp │

&#x20;                │   Cloud API   │

&#x20;                └───────┬───────┘

&#x20;                        │

&#x20;                        ▼

&#x20;                   💬 WhatsApp







\## 🛠️ Tech Stack



\### Backend



\* Python

\* FastAPI

\* Uvicorn

\* Pydantic

\* python-dotenv

\* Requests



\### AI Voice



\* OmniDimension



\### Messaging



\* Meta WhatsApp Cloud API



\### API Testing



\* FastAPI Swagger UI



\---



\## 📁 Project Structure



text

AI-Voice-Call-Agent/

│

├── backend/

│   └── main.py

│

├── frontend/

│   └── index.html

│

├── .gitignore

├── requirements.txt

└── README.md





> The `frontend` directory currently contains an early UI prototype. The primary interface for the current version is FastAPI's Swagger documentation.







\## ⚙️ Installation



\### 1. Clone the repository



bash

git clone https://github.com/Sahil-Bishnoi/AI-Voice-Call-Agent.git

cd AI-Voice-Call-Agent





\### 2. Create a virtual environment



Windows:



powershell

python -m venv venv

venv\\Scripts\\activate





macOS / Linux:



bash

python3 -m venv venv

source venv/bin/activate





\### 3. Install dependencies



bash

pip install -r requirements.txt





\---



\## 🔐 Environment Variables



Create:



text

backend/.env





Example:



env

OMNIDIM\_API\_KEY=your\_omnidimension\_api\_key

OMNIDIM\_AGENT\_ID=your\_agent\_id



META\_ACCESS\_TOKEN=your\_meta\_access\_token

PHONE\_NUMBER\_ID=your\_whatsapp\_phone\_number\_id





Never commit your `.env` file or expose API credentials publicly.



\---



\## ▶️ Running the Backend



From the project root:



powershell

python -m uvicorn backend.main:app --reload





The API will be available at:



text

http://127.0.0.1:8000





\### Swagger UI



Open:



text

http://127.0.0.1:8000/docs





Swagger provides an interactive interface for testing the API endpoints.



\---



\## 📞 Making an AI Voice Call



The main endpoint is:



text

POST /make-call





Example request:



json

{

&#x20;   "phone\_number": "+918570024429"

}





The backend:



1\. Receives the destination phone number.

2\. Validates/formats the number.

3\. Sends the call request to OmniDimension.

4\. OmniDimension dispatches the AI voice call.



Example successful response:



json{

&#x20;   "success": true,

&#x20;   "omnidimension\_response": {

&#x20;       "status": 200,

&#x20;       "json": {

&#x20;           "success": true,

&#x20;           "requestId": 6822971,

&#x20;           "status": "dispatched"

&#x20;       }

&#x20;   }

}





\---



\## 💬 WhatsApp Integration



The backend also provides:



text

POST /send-whatsapp





This endpoint communicates with the Meta WhatsApp Cloud API.



Example request:



json

{

&#x20;   "customer\_name": "Customer",

&#x20;   "phone\_number": "+918570024429",

&#x20;   "message": "Hello!"

}





The WhatsApp credentials are stored in environment variables.



\---



\## 🔌 API Endpoints



| Method | Endpoint           | Purpose                               |

| ------ | ------------------ | ------------------------------------- |

| GET    | `/`                | Backend health/status                 |

| GET    | `/app`             | Serves the current frontend prototype |

| POST   | `/make-call`       | Dispatches an AI voice call           |

| POST   | `/send-whatsapp`   | Sends a WhatsApp message              |

| POST   | `/omnidim-webhook` | Receives OmniDimension webhook events |



\---



\## 🔒 Security



Sensitive configuration is excluded from Git.



Ignored files include:



text

.env

venv/

\_\_pycache\_\_/

\*.log





Never commit:



\* API keys

\* Access tokens

\* Private credentials

\* Service authentication tokens



\---



\## 🚧 Current Development Status



\### Completed



\* \[x] FastAPI backend

\* \[x] OmniDimension integration

\* \[x] Dynamic phone number input through API

\* \[x] Outbound AI call dispatch

\* \[x] Swagger API interface

\* \[x] Meta WhatsApp API integration

\* \[x] Environment variable configuration

\* \[x] OmniDimension webhook endpoint



\### In Progress



\* \[ ] Interactive production frontend

\* \[ ] Call status tracking

\* \[ ] Call history

\* \[ ] Call transcripts

\* \[ ] AI-generated call summaries

\* \[ ] Automated WhatsApp follow-ups

\* \[ ] Mid-call intent detection

\* \[ ] Database integration

\* \[ ] User authentication

\* \[ ] Production deployment



\---



\## 🎯 Future Vision



The goal is to evolve the current backend prototype into a production-ready AI communication platform.



The planned system will allow users to manage contacts, initiate AI calls, monitor conversations, detect customer intent, generate call summaries, and automatically perform follow-up actions such as WhatsApp messaging.



\---



\## 👨‍💻 Author



\*\*Sahil Bishnoi\*\*



GitHub:

https://github.com/Sahil-Bishnoi



