from fastapi import FastAPI

app = FastAPI()


@app.get("/get-user")
async def get_user(name: str):
    return {"message": f"Hello"}
