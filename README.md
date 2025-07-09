# Health-Care-System Project 

A full-stack web application for hospitals to manage doctors, staff, patients, appointments, ambulance bookings, and an integrated E-medical shop.

## Features
- Doctor, staff, and patient management
- Appointment booking system
- Ambulance booking
- E-medical shop (cart, orders, payments)
- Nursing and room services
- User authentication (login/signup/password reset)
- Responsive UI (HTML, CSS, JS, Bootstrap)

---

## Technology Stack
- **Backend:** Python 3.9+, Django 3.2+
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Database:** SQLite (default), PostgreSQL (optional for production)
- **APIs:** Django REST Framework
- **Images:** Pillow

---

## Quick Start (Local)

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd Health-Care-System
   ```
2. **Create a virtual environment & activate:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply migrations:**
   ```bash
   python newproject/manage.py migrate
   ```
5. **Create superuser (admin):**
   ```bash
   python newproject/manage.py createsuperuser
   ```
6. **Run the development server:**
   ```bash
   python newproject/manage.py runserver
   ```
7. **Access the app:**
   - Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Docker Setup

1. **Build the Docker image:**
   ```bash
   docker build -t healthcare-system .
   ```
2. **Run the container:**
   ```bash
   docker run -p 8000:8000 healthcare-system
   ```
3. **Access the app:**
   - Visit [http://localhost:8000/](http://localhost:8000/)

---

## Kubernetes Demo

1. **Push your Docker image to Docker Hub:**
   - Update the image name in `k8s-demo.yaml` to your Docker Hub username.
2. **Apply the manifest:**
   ```bash
   kubectl apply -f k8s-demo.yaml
   ```
3. **Access the app:**
   - Use the external IP from your Kubernetes service (see `kubectl get svc`).

---

## Project Structure
- `newproject/` - Django project root
- `newapp/` - Main Django app (models, views, forms, etc.)
- `media/` - Uploaded images
- `static/` - Static files (CSS, JS, images)
- `templates/` - HTML templates
- `requirements.txt` - Python dependencies
- `Dockerfile` - Docker build instructions
- `k8s-demo.yaml` - Kubernetes deployment/service manifest

---

## Requirements
See [`requirements.txt`](./requirements.txt) for all Python dependencies.

---

![1](https://user-images.githubusercontent.com/91863955/143219583-b36ae52a-b2dc-4537-9511-9c25f211146d.png)

![2](https://user-images.githubusercontent.com/91863955/143219685-ada5e617-4807-4416-a4b7-681bdddeaca0.png)
![3](https://user-images.githubusercontent.com/91863955/143219695-51d12e89-b943-4e67-a641-1dbefcab4a88.png)
![4](https://user-images.githubusercontent.com/91863955/143219720-ee70241e-627e-4285-970e-dc2d4aa799dd.png)


![5](https://user-images.githubusercontent.com/91863955/143219740-5051bd38-d632-4749-a288-31edc4504da4.png)

![6](https://user-images.githubusercontent.com/91863955/143219759-013160bb-6139-4680-9950-67a915d401ba.png)

![8](https://user-images.githubusercontent.com/91863955/143219780-bae786b2-2487-413d-9d31-360debc14273.png)

![10](https://user-images.githubusercontent.com/91863955/143219822-689dd284-8def-4a02-b04b-21f8d737a512.png)


![Screenshot_2](https://user-images.githubusercontent.com/91863955/143220498-b624f215-3722-43af-a590-e5ea0cb6a1ad.png)


![a](https://user-images.githubusercontent.com/91863955/143219963-84346089-67b6-4976-8a0d-0333d6262461.png)
![b](https://user-images.githubusercontent.com/91863955/143219940-4a0449e5-41ec-4888-9aa3-00fb60494712.png)
![d](https://user-images.githubusercontent.com/91863955/143220010-80b96056-34ba-4546-af30-293e5dbdfe5a.png)
![e](https://user-images.githubusercontent.com/91863955/143220032-1ae78704-5d02-4341-9c95-b19a9ad1eccb.png)
![t](https://user-images.githubusercontent.com/91863955/143220062-a04d55cd-1e67-431d-82b4-fbc8711f21a0.png)
![o](https://user-images.githubusercontent.com/91863955/143220075-23f14757-b5d9-4bdd-aceb-c6535de8fd43.png)
![w](https://user-images.githubusercontent.com/91863955/143220084-bb8cd295-1224-4624-a727-99cc13c2c066.png)


