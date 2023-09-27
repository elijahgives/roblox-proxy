# Roblox Proxy
A simple proxy with FastAPI for getting some information from Roblox.

## Introduction

This proxy was created to streamline getting information from Roblox, like by combining multiple data requests into one response; it has a CORS (cross-origin resource sharing) handler so you can use it on websites without an issue.

## Installation and Setup
To run the Roblox Proxy on your machine, follow these steps:

### Clone the repository:

```bash
git clone https://github.com/elijahgives/roblox-proxy.git
```

### Install dependencies:

```bash
pip install -r requirements.txt
````
### Start the FastAPI development server:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
This will launch the FastAPI application, and it will be accessible at http://localhost:8000.

## Routes:
**GET** `/get-user?username={username}`
- `username`: the username of the Roblox user to get info for.
#### Get information on a roblox user.
### Example response
```json
{
  "requestedUsername": "roblox",
  "hasVerifiedBadge": true,
  "id": 1,
  "name": "Roblox",
  "displayName": "Roblox",
  "avatar": {
    "headshot": "https://tr.rbxcdn.com/ea3425c2b657de9af16c629441e0dcb2/420/420/AvatarHeadshot/Png"
  }
}
```
\
\
**GET** `/users/{user_id}/groups`
- `user_id`: the user ID of the Roblox user to list groups for.
#### Get the groups a Roblox user is in and their roles
### Example response
```json
{
  "data": [
    {
      "group": {
        "id": 7,
        "name": "Roblox",
        "memberCount": 10577659,
        "hasVerifiedBadge": false
      },
      "role": {
        "id": 52,
        "name": "Owner",
        "rank": 255
      }
    }
  ]
}
```
\
\
**GET** `/games/{game_id}`
- `game_id`: The place ID of the game to get information for.
  - This is the same that would be in the URL roblox.com/games/1083480314 <- place ID
#### Get information about a Roblox game.
### Example response
```json
{
  "id": 245662005,
  "rootPlaceId": 606849621,
  "name": "Jailbreak",
  "description": "Our next update launches early October!\n🏆 Jailbreak is a 12 time award winning game where you can orchestrate a robbery or catch criminals!",
  "sourceName": null,
  "sourceDescription": null,
  "creator": {
    "id": 3059674,
    "name": "Badimo",
    "type": "Group",
    "isRNVAccount": false,
    "hasVerifiedBadge": true
  },
  "price": null,
  "allowedGearGenres": [
    "TownAndCity"
  ],
  "allowedGearCategories": [],
  "isGenreEnforced": false,
  "copyingAllowed": false,
  "playing": 11128,
  "visits": 6525453918,
  "maxPlayers": 30,
  "created": "2017-01-06T16:39:11.173Z",
  "updated": "2023-09-27T16:41:23.0450258Z",
  "studioAccessToApisAllowed": false,
  "createVipServersAllowed": false,
  "universeAvatarType": "MorphToR15",
  "genre": "Town and City",
  "isAllGenre": false,
  "isFavoritedByUser": false,
  "favoritedCount": 17954433
}
```