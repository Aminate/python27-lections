from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def alco():
    return {"message":"just do it"}

@app.post("/create")
def create():
    return {"message":"created"}


@app.delete("/delete")
def delete():
    return {"message":"deleted"}