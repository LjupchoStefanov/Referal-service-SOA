from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    refferal_link = Column(String, unique=True, index=True)
    credits = Column(Float, default=0.0)
    administrator = Column(Boolean, default=False)
    refferaled_id = Column(Integer, ForeignKey('users.id'))


class Plan(Base):
    __tablename__ = "plans"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    num_servers = Column(Integer)
    price = Column(Float)


class Vaucher(Base):
    __tablename__ = "vaucher"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True)
    is_used = Column(Boolean, default=False)
    amount = Column(Float)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))


class PromoCode(Base):
    __tablename__ = "promo_code"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True)
    is_used = Column(Boolean, default=False)
    discount_percentage = Column(Float)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))