import aiohttp
from fastapi import FastAPI, HTTPException


app = FastAPI()


async def fetch_user_data(username: str, session: aiohttp.ClientSession):
    user_url = "https://users.roblox.com/v1/usernames/users"
    avatar_url = "https://thumbnails.roblox.com/v1/users/avatar-headshot"

    async with session.post(user_url, json={"usernames": [username]}) as user_response:
        user_data = await user_response.json()

    data = user_data.get('data', [])
    if len(data) == 0:
        raise HTTPException(status_code=404, detail="User not found")

    user_id = data[0].get("id")

    async with session.get(f"{avatar_url}?userIds={user_id}&size=420x420&format=Png&isCircular=false") as avatar_response:
        avatar_data = await avatar_response.json()

    avatar_url = avatar_data['data'][0]['imageUrl']

    user_data = data[0].copy()
    user_data['avatar'] = {'headshot': avatar_url}

    return user_data


@app.get("/get-user")
async def get_user(username: str):
    async with aiohttp.ClientSession() as session:
        user_data = await fetch_user_data(username, session)
        return user_data
