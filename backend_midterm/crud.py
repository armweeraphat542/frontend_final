from sqlalchemy.orm import Session
from . import models, schemas
from typing import List
from sqlalchemy import func
from fastapi import HTTPException


### Create

def create_trains(db: Session, trains: List[schemas.TrainCreate]):
    db_trains = []
    for train in trains:
        db_train = models.Train(**train.dict())
        db.add(db_train)
        db.commit()
        db.refresh(db_train)
        db_trains.append(db_train)
    return db_trains

def create_routes(db: Session, routes: List[schemas.RouteCreate]):
    created_routes = []
    for route in routes:
        db_route = models.Route(**route.dict())
        db.add(db_route)
        db.commit()
        db.refresh(db_route)
        created_routes.append(db_route)
    return created_routes


def create_stations(db: Session, stations: List[schemas.StationCreate]):
    created_stations = []
    for station in stations:
        db_station = models.Station(**station.dict())
        db.add(db_station)
        db.commit()
        db.refresh(db_station)
        created_stations.append(db_station)
    return created_stations


def create_stopstations(db: Session, stopstations: List[schemas.StopStationCreate]):
    created_stopstations = []
    for stopstation in stopstations:
        db_stopstation = models.StopStation(**stopstation.dict())
        db.add(db_stopstation)
        db.commit()
        db.refresh(db_stopstation)
        created_stopstations.append(db_stopstation)
    return created_stopstations


def create_routedetails(db: Session, route_details: list[schemas.RouteDetailCreate]):
    created_route_details = []
    for detail in route_details:
        db_detail = models.RouteDetail(**detail.dict())
        db.add(db_detail)
        db.commit()
        db.refresh(db_detail)
        created_route_details.append(db_detail)
    return created_route_details


def create_routeseatdetails(db: Session, seat_details: list[schemas.RouteSeatDetailCreate]):
    created_seat_details = []
    for seat_detail in seat_details:
        db_seat_detail = models.RouteSeatDetail(**seat_detail.dict())
        db.add(db_seat_detail)
        db.commit()
        db.refresh(db_seat_detail)
        created_seat_details.append(db_seat_detail)
    return created_seat_details


def create_traincars(db: Session, traincars: list[schemas.TrainCarCreate]):
    created_traincars = []
    for traincar in traincars:
        db_traincar = models.Traincar(**traincar.dict())
        db.add(db_traincar)
        db.commit()
        db.refresh(db_traincar)
        created_traincars.append(db_traincar)
    return created_traincars


def create_ticketorders(db: Session, ticket_orders: list[schemas.TicketOrderCreate]):
    created_orders = []
    for ticket_order in ticket_orders:
        db_order = models.TicketOrder(**ticket_order.dict())
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
        created_orders.append(db_order)
    return created_orders


def create_routeseatdetails(db: Session, seat_details: list[schemas.RouteSeatDetailCreate]):
    created_details = []
    for seat_detail in seat_details:
        db_detail = models.RouteSeatDetail(**seat_detail.dict())
        db.add(db_detail)
        db.commit()
        db.refresh(db_detail)
        created_details.append(db_detail)
    return created_details


def create_seatorders(db: Session, seat_orders: list[schemas.SeatOrderCreate]):
    created_orders = []
    for seat_order in seat_orders:
        db_order = models.SeatOrder(**seat_order.dict())
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
        created_orders.append(db_order)
    return created_orders


def create_customers(db: Session, customers: list[schemas.CustomerCreate]):
    created_customers = []
    for customer in customers:
        db_customer = models.Customer(**customer.dict())
        db.add(db_customer)
        db.commit()
        db.refresh(db_customer)
        created_customers.append(db_customer)
    return created_customers


### GET

def get_trains(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Train).offset(skip).limit(limit).all()

def get_routes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Route).offset(skip).limit(limit).all()


def get_stations(db: Session, skip: int = 0, limit: int = 20):
    return db.query(models.Station).offset(skip).limit(limit).all()


def get_stopstations(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.StopStation).offset(skip).limit(limit).all()


def get_routedetails(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.RouteDetail).offset(skip).limit(limit).all()


def get_routeseatdetails(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.RouteSeatDetail).offset(skip).limit(limit).all()


def get_traincars(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Traincar).offset(skip).limit(limit).all()


def get_ticketorders(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.TicketOrder).offset(skip).limit(limit).all()


def get_routeseatdetails(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.RouteSeatDetail).offset(skip).limit(limit).all()


def get_seatorders(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.SeatOrder).offset(skip).limit(limit).all()


def get_customers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Customer).offset(skip).limit(limit).all()

### UPDATE
def update_routeseatdetail(db: Session, traincarseat_id: str, updated_data: schemas.RouteSeatDetailUpdate):
    db_route_seat_detail = db.query(models.RouteSeatDetail).filter(models.RouteSeatDetail.traincarseat_id == traincarseat_id).first()
    if db_route_seat_detail:
        for key, value in updated_data.dict().items():
            setattr(db_route_seat_detail, key, value)
        db.commit()
        db.refresh(db_route_seat_detail)
        updated_route_seat_detail = db_route_seat_detail.__dict__
        updated_route_seat_detail.pop('_sa_instance_state', None)
        return "อัพเดทเรียบร้อย"
    else:
        raise HTTPException(status_code=404, detail="Route Seat Detail not found")

### โจทย์ข้อ 1
def get_route_station(db: Session, route_id: str):
    route_station_info = db.query(models.Route.route_name, models.Station.station_name, models.StopStation.arrival_time, models.StopStation.departure_time)\
             .join(models.StopStation, models.Route.route_id == models.StopStation.route_id
            ).join(models.Station, models.StopStation.station_id == models.Station.station_id
            ).filter(models.Route.route_id == route_id
            ).order_by(models.StopStation.arrival_time).all()
    
    return [
        {
            "route_name": row[0],
            "station_name": row[1],
            "arrival_time": row[2],
            "departure_time": row[3]
        }
        for row in route_station_info
    ]


### โจทย์ข้อ 2

def get_routesumtraincar(db: Session):
    sumtraincar = db.query(models.Route.route_name, func.sum(models.RouteDetail.traincar_quan).label("SumOftraincar_quan")
                    ).join(models.RouteDetail, models.Route.route_id == models.RouteDetail.route_id).group_by(models.Route.route_name).all()
    return [
        {
            "route_name": row[0],
            "SumOftraincar_quan": row[1]
        }
        for row in sumtraincar
    ]

def get_routesumtraincars(db: Session, route_id: str):
    sumtraincar = db.query(models.Route.route_name, func.sum(models.RouteDetail.traincar_quan).label("SumOftraincar_quan")
                    ).join(models.RouteDetail, models.Route.route_id == models.RouteDetail.route_id).group_by(models.Route.route_name
                    ).filter(models.Route.route_id == route_id).all()
    return [
        {
            "route_name": row[0],
            "SumOftraincar_quan": row[1]
        }
        for row in sumtraincar
    ]

def get_routedetailinfos(db: Session, route_id: str):
    route_detail = db.query( models.Route.route_name, models.Train.train_name, models.Traincar.traincar_name,
                    models.RouteDetail.traincar_quan, models.Traincar.traincar_seatpercar
                    ).join(models.RouteDetail, models.Route.route_id == models.RouteDetail.route_id
                    ).join(models.Traincar, models.RouteDetail.traincar_id == models.Traincar.traincar_id
                    ).join(models.Train, models.Route.train_id == models.Train.train_id
                    ).filter(models.Route.route_id == route_id).all()
    return [
        {
            "route_name": row[0],
            "train_name": row[1],
            "traincar_name": row[2],
            "traincar_quan": row[3],
            "traincar_seatpercar": row[4]
        }
        for row in route_detail
    ]

###โจทย์ข้อ 3
def get_ticketdetails(db:Session):
    ticket_detail = db.query(models.TicketOrder.ticket_id, models.Route.route_name, models.Train.train_name, models.Route.route_date,
                    models.Traincar.traincar_name, models.TicketOrder.order_quan,).join((models.Route, models.Route.route_id == models.TicketOrder.route_id),
                    (models.Traincar, models.TicketOrder.traincar_id == models.Traincar.traincar_id)
                    ).join(models.Train, models.Route.train_id == models.Train.train_id
                    ).all()
    return [
        {
            "ticket_id": row[0],
            "route_name": row[1],
            "train_name": row[2],
            "route_date": row[3],
            "traincar_name": row[4],
            "order_quan": row[5]
        }
        for row in ticket_detail
    ]

def get_ticketdetail(db:Session, route_id: str):
    ticket_detail = db.query(models.TicketOrder.ticket_id, models.Route.route_name, models.Train.train_name, models.Route.route_date,
                    models.Traincar.traincar_name, models.TicketOrder.order_quan,).join((models.Route, models.Route.route_id == models.TicketOrder.route_id),
                    (models.Traincar, models.TicketOrder.traincar_id == models.Traincar.traincar_id)
                    ).join(models.Train, models.Route.train_id == models.Train.train_id
                    ).filter(models.Route.route_id == route_id).all()
    return [
        {
            "ticket_id": row[0],
            "route_name": row[1],
            "train_name": row[2],
            "route_date": row[3],
            "traincar_name": row[4],
            "order_quan": row[5]
        }
        for row in ticket_detail
    ]


###โจทย์ข้อ 4
def get_seatrorderdetail(db: Session, route_id: str):
    seat_detail = db.query(models.TicketOrder.ticket_id, models.Route.route_name, models.Train.train_name, models.Traincar.traincar_name, models.SeatOrder.traincarseat_id).join(models.Route, models.TicketOrder.route_id == models.Route.route_id
                    ).join(models.SeatOrder, models.TicketOrder.ticket_id == models.SeatOrder.ticket_id
                    ).join(models.RouteSeatDetail, models.RouteSeatDetail.traincarseat_id == models.SeatOrder.traincarseat_id
                    ).join(models.Traincar, models.TicketOrder.traincar_id == models.Traincar.traincar_id
                    ).join(models.Train, models.Route.train_id == models.Train.train_id
                    ).filter(models.Route.route_id == route_id).all()
    return [
        {
            "ticket_id": row[0],
            "route_name": row[1],
            "train_name": row[2],
            "traincar_name": row[3],
            "traincarseat_id": row[4] 
        }
        for row in seat_detail
    ]