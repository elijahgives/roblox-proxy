import aiohttp
from fastapi import HTTPException


async def get_user_data(username: str, session: aiohttp.ClientSession):
    """Get information about a Roblox user by their username."""
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
    """Get a list of a user's groups and their roles in them."""
    async with session.get(f"https://groups.roblox.com/v2/users/{user_id}/groups/roles") as response:
        data = await response.json()
        return data


async def get_game_info(game_id: int, session: aiohttp.ClientSession):
    """Get information on a game from its place ID."""
    async with session.get(f"https://apis.roblox.com/universes/v1/places/{game_id}/universe") as response:
        data = await response.json()
        if data.get("universeId") is None:
            raise HTTPException(status_code=404, detail="Not found")
        universe_id = data.get("universeId")
    async with session.get(f"https://games.roblox.com/v1/games?universeIds={universe_id}") as game_response:
        game_data = (await game_response.json())["data"][0].copy()
    async with session.get(f"https://thumbnails.roblox.com/v1/games/icons?universeIds={game_data['id']}&returnPolicy=PlaceHolder&size=512x512&format=Png&isCircular=false") as icon_response:
        icon_data = (await icon_response.json())["data"][0]
        game_data["assets"] = {"icon": icon_data["imageUrl"]}
    async with session.get(f"https://thumbnails.roblox.com/v1/games/multiget/thumbnails?universeIds={game_data['id']}&countPerUniverse=50&defaults=true&size=768x432&format=Png&isCircular=false") as thumbnail_response:
        thumbnail_data = (await thumbnail_response.json())["data"][0]
        game_data["assets"]["thumbnails"] = [thumbnail["imageUrl"] for thumbnail in thumbnail_data["thumbnails"]]
    return game_data

