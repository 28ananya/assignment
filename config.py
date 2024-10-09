from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or 'your_fallback_secret_key'
    MONGO_URI = 'mongodb://localhost:27017/assignment_portal'
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY') or 'your_fallback_jwt_secret_key'
