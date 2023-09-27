import aiohttp
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from utils.roblox import fetch_user_data


app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/get-user")
async def get_user(username: str):
    async with aiohttp.ClientSession() as session:
        user_data = await fetch_user_data(username, session)
        return user_data
