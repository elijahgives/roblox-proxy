# Roblox Proxy
A simple Roblox proxy with FastAPI for getting some information.

## Routes:
`/get-user?username={username}`
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

`/users/{user_id}/groups`
- `user_id`: the user ID of the Roblox user to list groups for.
- #### Get the groups a Roblox user is in and their roles
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