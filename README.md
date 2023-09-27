# Roblox Proxy
A simple Roblox proxy with FastAPI for getting some information.

## Routes:
`/get-user?username={username}`
- `username`: the username of the Roblox user to get info for.
#### Get information on a roblox user. Example response:
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