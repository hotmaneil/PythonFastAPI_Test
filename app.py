from fastapi import FastAPI

app = FastAPI()


stuffed_toys = []

# Hello World 端


@app.get("/")
def hello_world():
    return {"message": "hi"}


@app.get("toys",
         summary="取得玩具清單",
         description="取得一大堆玩具的清單",
         tags=["玩具"])
def get_toys():
    return {"stuffed toys": stuffed_toys}


@app.post("/toys")
def add_toy(toy):
    stuffed_toys.append(toy)
    return {"message": f"Toy '{toy} added successfully!'"}
