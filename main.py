from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    email: str


@app.get("/")
def root_router():
    return {"message": "Hello World"}


@app.put(
    "/user",
    summary="Kafka Connect로 부터 user 정보를 받습니다.",
)
def consume_user(user: User):
    print("user: ", user)
    return user
