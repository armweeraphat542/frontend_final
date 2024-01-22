from fastapi import FastAPI
from pydantic import BaseModel

class Tour(BaseModel):
    name: str
    destination: str
    price: float
    banner: str

app = FastAPI()

@app.post("/tour/")
async def create_tour(tour: Tour) -> Tour:
    print(tour)
    tour.price -= 50
    return tour

@app.get("/tours")
async def read_all_tour() -> list[Tour]:
    return[
        Tour(name="Yuttaya", destination="Thailand", price=3999, banner="Watyutya.jpg"),
        Tour(name="WatPo", destination="Thailand", price=1500, banner="WatPo.jpg"),
    ]

@app.get("/tour/{tourId}")
async def read_tour(tourId: int):
    return {"tourId": tourId}