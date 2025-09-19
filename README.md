# 🚀 FastAPI Login Backend (Sample)

This is a simple backend authentication system built with **FastAPI**.  
It demonstrates how to implement user login, authentication, and token handling in a clean and minimal way.  

---

## 🔧 Tech Stack
- [FastAPI](https://fastapi.tiangolo.com/) – Modern, fast (high-performance), web framework for Python  
- [Uvicorn](https://www.uvicorn.org/) – ASGI server for running FastAPI apps  
- [Pydantic](https://docs.pydantic.dev/) – Data validation and settings management  
- [JWT (JSON Web Tokens)](https://jwt.io/) – For secure authentication  

---

## 📂 Project Structure
fastapi-login-sample/
  │── app/
  │ ├── main.py # Entry point of the app
  │ ├── auth.py # Authentication & JWT logic
  │ ├── models.py # User models & schemas
  │ ├── database.py # (Optional) Database connection
  │── requirements.txt # Project dependencies
  │── README.md # Project documentation



---

## ⚡ Getting Started

### 1️⃣ Clone the repo
  - git clone https://github.com/your-username/fastapi-login-sample.git
  - cd fastapi-login-sample
### 2️⃣ Create a virtual environment
  - python -m venv venv
  - source venv/bin/activate   # On Linux / Mac
  - venv\Scripts\activate      # On Windows
    
### 3️⃣ Install dependencies

  - pip install -r requirements.txt

### 4️⃣ Run the server

  - uvicorn app.main:app --reload
- Server will start at 👉 http://127.0.0.1:8000

### 🔑 API Endpoints
  - Method	Endpoint	Description	Auth Required
  - POST	/login	User login with creds	❌
  - GET	/profile	Get user profile	✅ JWT Token
  - POST	/register	Register a new user	❌

### 📖 Example Login Flow
- User sends credentials to /login

- Backend verifies and returns a JWT token

- Client uses this token for protected endpoints (e.g., /profile)

### 🛠️ Future Improvements
1. Add refresh tokens

2. Hash passwords using passlib

3. Add role-based authorization

### 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

### 📜 License
This project is licensed under the MIT License.


---


