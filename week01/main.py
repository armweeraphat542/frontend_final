from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"Hellow World"}

@app.get("/get_customer")
def get_customer():
    return { 
        "cus01":"Pim",
        "cus02": "Arm",
    }
