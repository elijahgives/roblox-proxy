import aiohttp
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from utils.roblox import get_user_data, get_user_groups, get_game_info


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
        user_data = await get_user_data(username, session)
        return user_data


@app.get("/users/{user_id}/groups")
async def get_groups(user_id: int):
    async with aiohttp.ClientSession() as session:
        groups = await get_user_groups(user_id, session)
        return groups


@app.get("/games/{game_id}")
async def get_game(game_id: int):
    async with aiohttp.ClientSession() as session:
        game = await get_game_info(game_id, session)
        return game
