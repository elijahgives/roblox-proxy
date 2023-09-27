import aiohttp
from fastapi import HTTPException


async def get_user_data(username: str, session: aiohttp.ClientSession):
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


async def get_user_groups(user_id: int, session: aiohttp.ClientSession):
    async with session.get(f"https://groups.roblox.com/v2/users/{user_id}/groups/roles") as response:
        data = await response.json()
        return data
