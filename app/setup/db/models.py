from sqlalchemy import Column, DateTime, func, BigInteger

from app.setup.db import db


class Base(db.Model):
    __abstract__ = True

    created = Column(DateTime, nullable=False, default=func.now())
    updated = Column(DateTime, default=func.now(), onupdate=func.now())


class BaseWithID(Base):
    __abstract__ = True

    id = Column(BigInteger, primary_key=True, autoincrement=True)


class BaseManyToMany(Base):
    __abstract__ = True
