# Documentation – meu_projeto_async

This project demonstrates how to create asynchronous views in Django (version 5.1.7) and shows how to set up simple routes for testing and learning purposes.

## Table of Contents
1. [Overview](#overview)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Project Structure](#project-structure)
5. [Virtual Environment Setup](#virtual-environment-setup)
6. [Running the Project](#running-the-project)
7. [Usage Example (Route `/contar/`)](#usage-example-route-contar)
8. [Running in ASGI Mode](#running-in-asgi-mode)
9. [References](#references)

---

## 1. Overview

**meu_projeto_async** 
is created to demonstrate how to write an asynchronous view in Django and run the application both using the built-in Django development server (WSGI mode) and an ASGI server (like Uvicorn).

### Key Features
- **Asynchronous view** using `async/await`
- **Basic routes** for testing (`/` and `/contar/`)
- **Example counter** using `asyncio.sleep()` to illustrate non-blocking behavior
- **Compatible with Django 5.1.7**

---

## 2. Requirements

- **Python 3.10+** (recommended: 3.12 or higher)
- **Django 5.1.7**
- (Optional) **Uvicorn** or another ASGI server if you want to run in full asynchronous mode

---

## 3. Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your_username/meu_projeto_async.git
  
    cd meu_projeto_async
  
    python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

pip install -r requirements.txt
pip install uvicorn httpx

## Project Ptructure

meu_projeto_async/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── venv/                (virtual environment folder)
├── minha_app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   └── views.py
└── meu_projeto_async/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

## Virtual Environment Setup 

python -m venv venv
# Activate on Windows:
venv\Scripts\activate
# Activate on Linux/Mac:
source venv/bin/activate

pip install -r requirements.txt

## Running the Project 

1  **Activate your virtual environment (if not already activated).** 

2 **Run the serve:**

 python manage.py runserver

3 **Open your browser and navigate to** 
http://127.0.0.1:8000

## 7 Usage Example (Route /contar/) 
 **In the file minha_app/views.py, you have an asynchronous example function:**
 import asyncio
from django.http import HttpResponse

async def contador_de_tempo(request):
    for i in range(5):
        print(f"Count: {i}")
        await asyncio.sleep(1)
    return HttpResponse("Count completed!")

**To test the asynchronous view, navigate to:**
http://127.0.0.1:8000/contar/


## 8 Running in ASGI Mode 

**To fully run the application in asynchronous mode, use an ASGI server (e.g., Uvicorn):**
1. **Install Uvicorn:** 
pip install uvicorn
2. **Ensure your settings.py includes:**
ASGI_APPLICATION = 'meu_projeto_async.asgi.application'
3. **Run the application with Uvicorn:**
uvicorn meu_projeto_async.asgi:application --host 127.0.0.1 --port 8000
4. **Navigate to:** 
http://127.0.0.1:8000/contar/
 
*Now, Django will use the ASGIHandler, allowing your asynchronous views to truly leverage the event loop and handle multiple requests concurrently.*

## 9 References 
    - https://docs.djangoproject.com/en/5.1/topics/async/ (Django)
    -  https://www.uvicorn.org/ (Uvicorn)
    - https://github.com/django/daphne (Daphne)
