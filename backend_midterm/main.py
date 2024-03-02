from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from typing import  List, Dict, Union
from fastapi.responses import JSONResponse


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


### POST
        
@app.post("/trains/", response_model=List[schemas.TrainCreate])
def create_trains(trains: List[schemas.TrainCreate], db: Session = Depends(get_db)):
    return crud.create_trains(db=db, trains=trains)


@app.post("/routes/", response_model=List[schemas.Route])
def create_routes(routes: List[schemas.RouteCreate], db: Session = Depends(get_db)):
    return crud.create_routes(db, routes)

@app.post("/stations/", response_model=List[schemas.Station])
def create_stations(stations: List[schemas.StationCreate], db: Session = Depends(get_db)):
    return crud.create_stations(db, stations)

@app.post("/stopstations/", response_model=List[schemas.StopStation])
def create_stopstations(stopstations: List[schemas.StopStationCreate], db: Session = Depends(get_db)):
    return crud.create_stopstations(db, stopstations)

@app.post("/routedetails/", response_model=list[schemas.RouteDetailCreate])
def create_routedetails(route_details: list[schemas.RouteDetailCreate], db: Session = Depends(get_db)):
    return crud.create_routedetails(db, route_details)


@app.post("/routeseatdetails/", response_model=list[schemas.RouteSeatDetailCreate])
def create_routeseatdetails(seat_details: list[schemas.RouteSeatDetailCreate], db: Session = Depends(get_db)):
    return crud.create_routeseatdetails(db, seat_details)

@app.post("/traincars/", response_model=list[schemas.TrainCarCreate])
def create_traincars(traincars: list[schemas.TrainCarCreate], db: Session = Depends(get_db)):
    return crud.create_traincars(db, traincars)

@app.post("/ticketorders/", response_model=list[schemas.TicketOrderCreate])
def create_ticket_orders(ticket_orders: list[schemas.TicketOrderCreate], db: Session = Depends(get_db)):
    return crud.create_ticketorders(db=db, ticket_orders=ticket_orders)

@app.post("/routeseatdetails/", response_model=list[schemas.RouteSeatDetail])
def create_route_seat_details(seat_details: list[schemas.RouteSeatDetailCreate], db: Session = Depends(get_db)):
    return crud.create_routeseatdetails(db=db, seat_details=seat_details)

@app.post("/seatorders/", response_model=List[schemas.SeatOrder])
def create_seat_orders(seat_orders: List[schemas.SeatOrderCreate], db: Session = Depends(get_db)):
    return crud.create_seatorders(db=db, seat_orders=seat_orders)


@app.post("/customers/", response_model=list[schemas.Customer])
def create_customers(customers: list[schemas.CustomerCreate], db: Session = Depends(get_db)):
    return crud.create_customers(db=db, customers=customers)



### GET

@app.get("/trains/", response_model=list[schemas.Train])
def read_trains(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_trains(db, skip=skip, limit=limit)

@app.get("/routes/", response_model=List[schemas.Route])
def read_routes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_routes(db, skip=skip, limit=limit)


@app.get("/stations/", response_model=List[schemas.Station])
def read_stations(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    return crud.get_stations(db, skip=skip, limit=limit)


@app.get("/stopstations/", response_model=List[schemas.StopStation])
def read_stopstations(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_stopstations(db, skip=skip, limit=limit)

@app.get("/routedetails/", response_model=list[schemas.RouteDetail])
def read_routedetails(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_routedetails(db, skip=skip, limit=limit)

@app.get("/routeseatdetails/", response_model=list[schemas.RouteSeatDetail])
def read_routeseatdetails(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_routeseatdetails(db, skip=skip, limit=limit)

@app.get("/traincars/", response_model= List[schemas.TrainCar])
def read_traincars(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_traincars(db, skip=skip, limit=limit)

@app.get("/ticketorders/", response_model=list[schemas.TicketOrder])
def read_ticket_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)): 
    return crud.get_ticketorders(db, skip=skip, limit=limit)

@app.get("/customers/", response_model=list[schemas.Customer])
def read_customers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_customers(db, skip=skip, limit=limit)

@app.get("/routeseatdetails/", response_model=list[schemas.RouteSeatDetail])
def read_route_seat_details(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_routeseatdetails(db, skip=skip, limit=limit)

@app.get("/seatorders/", response_model=List[schemas.SeatOrder])
def read_seat_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_seatorders(db, skip=skip, limit=limit)

### Update
@app.put("/routeseatdetails/{traincarseat_id}", response_model=schemas.RouteSeatDetail)
def update_route_seat_detail(traincarseat_id: str, updated_data: schemas.RouteSeatDetailUpdate, db: Session = Depends(get_db)):
    updated_route_seat_detail = crud.update_routeseatdetail(db=db, traincarseat_id=traincarseat_id, updated_data=updated_data)
    return JSONResponse(content=updated_route_seat_detail)

## GET โจทยข้อ 1
@app.get("/routestationinfo/{route_id}", response_model=list[Dict[str, Union[str, int]]])
def read_routestationinfo(route_id: str, db: Session = Depends(get_db)):
    route_stationinfo = crud.get_route_station(db=db, route_id=route_id)
    return route_stationinfo



## GET โจทยข้อ 2
@app.get("/routetraincarsums/", response_model=list[Dict[str, Union[str, int]]])
def read_routetraincarsum(db: Session = Depends(get_db)):
    route_traincar_summary = crud.get_routesumtraincar(db)
    return route_traincar_summary

@app.get("/routetraincarsum/{route_id}", response_model=list[Dict[str, Union[str, int]]])
def read_routetraincarsum(route_id: str, db: Session = Depends(get_db)):
    route_traincar_summary = crud.get_routesumtraincars(db=db, route_id=route_id)
    return route_traincar_summary


@app.get("/routetraincardetail/{route_id}", response_model=List[Dict[str, Union[str, int]]])
def read_routetraincardetail(route_id: str, db: Session = Depends(get_db)):
    route_routetraincardetail = crud.get_routedetailinfos(db=db, route_id=route_id)
    return route_routetraincardetail

## GET โจทยข้อ 3
@app.get("/ticketorderdetails/", response_model=List[Dict[str, Union[str, int]]])
def read_ticket_orders(db: Session = Depends(get_db)):
    ticket_orders = crud.get_ticketdetails(db)
    return ticket_orders

@app.get("/ticketorderdetail/{route_id}", response_model=List[Dict[str, Union[str, int]]])
def read_ticket_orders(route_id: str, db: Session = Depends(get_db)):
    ticket_orders = crud.get_ticketdetail(db=db, route_id=route_id)
    return ticket_orders

## GET โจทยข้อ 4
@app.get("/seatorderdetail/{route_id}", response_model=list[Dict[str, Union[str, int]]])
def seat_orderdetail(route_id: str, db: Session = Depends(get_db)):
    seat_detail = crud.get_seatrorderdetail(db=db, route_id=route_id)
    return seat_detail