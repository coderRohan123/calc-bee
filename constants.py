from dotenv import load_dotenv
import os
load_dotenv()

SERVER_URL = 'https://calc-bee.vercel.app'
PORT = '443'
ENV = 'prod'

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
