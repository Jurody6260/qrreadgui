from sqlalchemy import func, and_, delete,create_engine, text, MetaData, Integer, String, Column, ForeignKey, Date, Time, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, subqueryload, joinedload, relationship
from datetime import date, time, datetime

meta = MetaData()
Base = declarative_base()
engine = create_engine("sqlite:///qrco.db")

Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    tel = Column(String, nullable=False)
    entered_on = Column(DateTime, nullable=False)
    payed = Column(Integer, nullable=False)
    insideNOW = Column(Boolean, nullable=False, default=False)
    #payment = relationship("Payment", back_populates="user")

    def __repr__(self):
        return super().__repr__()


Base.metadata.create_all(bind=engine)
session.close()