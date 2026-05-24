from fastapi import FastAPI                         
from fastapi.middleware.cors import CORSMiddleware  
from app.routes import users                      

app = FastAPI(title="User API")   # Title appears in /docs

# Middleware to allow cross-origin requests from any origin, which is useful for development and testing. In production, you should specify allowed origins for security reasons.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)   

# Health check endpoint to verify the API is running
@app.get("/")
def health_check():
    return {"status": "ok"}