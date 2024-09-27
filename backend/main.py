
from openai import OpenAI
from dotenv import load_dotenv
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
aiapikey: str = os.environ["OPENAI_API_KEY"]
client = OpenAI(api_key = aiapikey)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def get_default():
    return "Home"

@app.post("/hello")
async def say_hello():

    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Respond to me saying hello!"}
    ]
    )

    return completion.choices[0].message