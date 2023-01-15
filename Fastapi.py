import datetime
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/user1/{message}")
def read_root(message):
    f = open("user1.txt", "a",encoding="utf-8")
    f.write("\n")
    f.write(str(datetime.datetime.now()))
    f.write("\n")
    f.write(message)
    f.close()

@app.get("/user2/{message}")
def read_root(message):
    f = open("user2.txt","a",encoding="utf-8")
    f.write("\n")
    f.write(str(datetime.datetime.now()))
    f.write("\n")
    f.write(message)
    f.close()

@app.get("/")
def read_root():
    return {"user1 Message : ":open("user1.txt","r").read(),"user2 Message : ":open("user2.txt","r").read()}
@app.get("/user1clearmessage")
def read_root():
    f = open("user1.txt", "w",encoding="utf-8")
    f.write("")
    f.close()
@app.get("/user2clearmessage")
def read_root():
    f = open("user2.txt", "w")
    f.write("")
    f.close()
if __name__ == "__main__":
    config = uvicorn.Config(app, port=5000, log_level="info",reload=True)
    server = uvicorn.Server(config)
    server.run()