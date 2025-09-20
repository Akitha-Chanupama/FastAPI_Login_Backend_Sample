from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from auth import router as auth_router  # your login route

app = FastAPI()

# 🔐 Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include your routers after middleware setup
app.include_router(auth_router, prefix="/auth")

# Add a simple root endpoint for testing
@app.get("/")
def read_root():
    return {"message": "FastAPI server is running!"}

# Add a debug endpoint to see all routes
@app.get("/debug/routes")
def get_routes():
    routes = []
    for route in app.routes:
        if hasattr(route, 'methods') and hasattr(route, 'path'):
            routes.append({
                "path": route.path,
                "methods": list(route.methods)
            })
    return {"routes": routes}

# Print available routes on startup
@app.on_event("startup")
def startup_event():
    print("\n" + "="*50)
    print("🚀 SERVER STARTED SUCCESSFULLY!")
    print("="*50)
    print("Available routes:")
    for route in app.routes:
        if hasattr(route, 'methods') and hasattr(route, 'path'):
            methods = [method for method in route.methods if method != 'HEAD']
            if methods:
                print(f"  {', '.join(methods)} {route.path}")
    print("="*50)
    print("Test endpoints:")
    print("  Root: http://172.16.200.58:8000/")
    print("  Docs: http://172.16.200.58:8000/docs")
    print("  Login: http://172.16.200.58:8000/auth/login")
    print("="*50 + "\n")
