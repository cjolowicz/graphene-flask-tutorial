from typing import Any
import sqlalchemy as sa
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = sa.create_engine("sqlite:///database.sqlite3", convert_unicode=True)
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base: Any = declarative_base()
Base.query = session.query_property()


class Department(Base):
    __tablename__ = "department"
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)


class Employee(Base):
    __tablename__ = "employee"
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    hired_on = sa.Column(sa.DateTime, default=sa.func.now())
    department_id = sa.Column(sa.Integer, sa.ForeignKey("department.id"))
    department = relationship(
        Department, backref=backref("employees", uselist=True, cascade="delete,all")
    )
