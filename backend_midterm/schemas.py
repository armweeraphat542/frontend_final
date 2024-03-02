from pydantic import BaseModel
from typing import Optional, List


class Train(BaseModel):
    train_id: str
    train_name: str

class TrainCreate(Train):
    pass

    class Config:
        orm_mode = True

class Customer(BaseModel):
    cust_id: str
    cust_name: str

class CustomerCreate(Customer):
    pass

    class Config:
        orm_mode = True

####
class Station(BaseModel):
    station_id: str
    station_name: str


class StationCreate(Station):
    pass

    class Config:
        orm_mode = True

####
class Route(BaseModel):
    route_id: str
    route_name: str
    train_id : str
    startstation_id: str
    endingstation_id: str
    route_date: str

class RouteCreate(Route):
    pass

    class Config:
        orm_mode = True

####
class RouteDetail(BaseModel):
    routedetail_id: str
    route_id: str
    traincar_id: str
    traincar_quan: int

class RouteDetailCreate(RouteDetail):
    pass

    class Config:
        orm_mode = True

####
class RouteSeatDetail(BaseModel):
    routedetail_id: str
    traincar_id: str
    traincarseat_id: str
    seat_status: str

class RouteSeatDetailCreate(RouteSeatDetail):
    pass

class RouteSeatDetailUpdate(RouteSeatDetail):
    pass

    class Config:
        orm_mode = True

####
class SeatOrder(BaseModel):
    ticket_id: str
    traincarseat_id: str

class SeatOrderCreate(SeatOrder):
    pass

    class Config:
        orm_mode = True

####
class StopStation(BaseModel):
    route_id: str
    station_id: str
    arrival_time: str
    departure_time: str

class StopStationCreate(StopStation):
    pass

    class Config:
        orm_mode = True

####
class TicketOrder(BaseModel):
    ticket_id: str
    cust_id: str
    route_id: str
    traincar_id: str
    order_date: str
    order_quan: int
    price: int

class TicketOrderCreate(TicketOrder):
    pass

    class Config:
        orm_mode = True

####
class TrainCar(BaseModel):
    traincar_id: str
    traincar_name: str
    traincar_seatpercar: int

class TrainCarCreate(TrainCar):
    pass

    class Config:
        orm_mode = True