from sqlalchemy import Column, ForeignKey, Integer, String, Time
from sqlalchemy.orm import relationship
from .database import Base



class Train(Base):
    __tablename__ = 'train'
    train_id = Column(String, primary_key=True, index=True)
    train_name = Column(String)

    route = relationship("Route", back_populates="train")


class Customer(Base):
    __tablename__ = 'customers'
    cust_id = Column(String, primary_key=True, index=True)
    cust_name = Column(String)

class Station(Base):
    __tablename__ = 'station'
    station_id = Column(String, primary_key=True, index=True)
    station_name = Column(String)

    stop_stations = relationship("StopStation", back_populates="station")

class Route(Base):
    __tablename__ = 'route'
    route_id = Column(String, primary_key=True, index=True)
    route_name = Column(String)
    train_id = Column(String, ForeignKey('train.train_id'))
    startstation_id = Column(String, ForeignKey('station.station_id'))
    endingstation_id = Column(String, ForeignKey('station.station_id'))
    route_date =Column(String)
    
    train = relationship("Train", back_populates="route")
    start_station = relationship("Station", foreign_keys=[startstation_id])
    ending_station = relationship("Station", foreign_keys=[endingstation_id])
    route_details = relationship("RouteDetail", back_populates="route")

class RouteDetail(Base):
    __tablename__ = 'routedetail'
    routedetail_id = Column(String, primary_key=True, index=True)
    route_id = Column(String, ForeignKey('route.route_id'), primary_key=True)
    traincar_id = Column(String, ForeignKey('traincar.traincar_id'), primary_key=True)
    traincar_quan = Column(Integer)

    route = relationship("Route", back_populates="route_details")

class RouteSeatDetail(Base):
    __tablename__ = 'routeseatdetails'
    routedetail_id = Column(String, ForeignKey('routedetail.routedetail_id'), primary_key=True)
    traincar_id = Column(String, ForeignKey('traincar.traincar_id'), primary_key=True)
    traincarseat_id = Column(String, primary_key=True)
    seat_status = Column(String)

class SeatOrder(Base):
    __tablename__ = 'seatorder'
    ticket_id = Column(String, ForeignKey('ticketorder.ticket_id'), primary_key=True)
    traincarseat_id = Column(String, ForeignKey('routeseatdetails.traincarseat_id'), primary_key=True)


    orderid = relationship("TicketOrder", back_populates="seatno")

class StopStation(Base):
    __tablename__ = 'stopstation'
    route_id = Column(String, ForeignKey('route.route_id'), primary_key=True)
    station_id = Column(String, ForeignKey('station.station_id'), primary_key=True)
    arrival_time = Column(String)
    departure_time = Column(String)

    station = relationship("Station", back_populates="stop_stations")

class TicketOrder(Base):
    __tablename__ = 'ticketorder'
    ticket_id = Column(String, primary_key=True, index=True)
    cust_id = Column(String, ForeignKey('customers.cust_id'))
    route_id = Column(String, ForeignKey('route.route_id'))
    traincar_id = Column(String, ForeignKey('traincar.traincar_id'))
    order_date = Column(String)
    order_quan = Column(Integer)
    price = Column(Integer)

    seatno = relationship("SeatOrder", back_populates="orderid")

class Traincar(Base):
    __tablename__ = 'traincar'
    traincar_id = Column(String, primary_key=True, index=True)
    traincar_name = Column(String)
    traincar_seatpercar = Column(Integer)