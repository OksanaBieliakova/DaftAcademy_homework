from fastapi import FastAPI, Request

from pydantic import BaseModel

app = FastAPI()
# to see what funny will come
app.counter = 0

class RespMethod(BaseModel):
    method: str


class HelloResp(BaseModel):
    message: str


class GiveMeSomethingRq(BaseModel):
    first_key: str


class GiveMeSomethingResp(BaseModel):
    received: dict
    constant_data: str = "python jest super"


@app.get('/counter')
def counter():
    app.counter += 1
    return app.counter


@app.get("/hello/{name}", response_model=HelloResp)
def read_item(name: str):
    return HelloResp(message=f"Hello {name}")


@app.post("/give/me/smth", response_model=GiveMeSomethingResp)
def receive_something(rq: GiveMeSomethingRq):
    return GiveMeSomethingResp(received=rq.dict())


@app.get("/", response_model=HelloResp)
def root():
    return HelloResp(message="Hello World during the coronavirus pandemic!")


@app.get("/method", response_model=RespMethod)
@app.post("/method", response_model=RespMethod)
@app.put("/method", response_model=RespMethod)
@app.delete("/method", response_model=RespMethod)
def method_get(req: Request):
    return RespMethod(method=req.method)