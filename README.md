# 🧠 SignAI Service  
*A FastAPI-based microservice for sign language recognition using AI.*

---

## 📌 Overview  
**SignAI Service** is a lightweight and modular microservice built with **FastAPI** designed to perform **sign language recognition**.  
It provides a clean architecture that separates API routing, configuration, and business logic, making it easy to extend with machine learning models, gesture keypoints, or video processing pipelines.

The service is intended to be the AI backend of a full-stack application that helps users detect, interpret, or learn sign language gestures.

---

## 🏗 Project Architecture  
signai_service/
├── app/
│ ├── api/
│ │ ├── init.py
│ │ ├── routes.py
│ │ └── controllers.py
│ ├── core/
│ │ ├── init.py
│ │ └── config.py
│ └── services/
│ └── predict_service.py
├── tests/
│ ├── init.py
│ ├── test_routes.py
│ └── test_services.py
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md


---

## 📁 Folder Explanation  

| Folder | Purpose |
|--------|---------|
| `app/api` | API endpoints (routes + controllers) |
| `app/core` | Environment settings, configuration, and future security layers |
| `app/services` | Business logic (ML models, prediction functions, pipelines) |
| `tests` | Unit tests for endpoints and services |
| `.env` | Environment variables |
| `main.py` | FastAPI entry point |

