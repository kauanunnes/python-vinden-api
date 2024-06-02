from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from enum import Enum as PyEnum
from sqlalchemy.dialects.postgresql import ENUM as PostgreSQLEnum
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class CompanyRole(PyEnum):
    BAR = 'bar'
    RESTAURANT = 'restaurant'
    PUB = 'pub'
    CAFE = 'cafe'

    def __str__(self):
        return self.value


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    login = Column(String(100), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(64), nullable=False)
    phone = Column(String(100), nullable=True)
    
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'login': self.login,
            'phone': self.phone,
            'created_on': self.created_on,
            'updated_on': self.updated_on
        }
    
class Person(Base):
    __tablename__ = 'people'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    cpf = Column(String(11), nullable=False, unique=True)
      
    birthday = Column(DateTime(), nullable=False)
    
    user_id = Column(Integer(), ForeignKey('users.id'))

    def to_dict(self):
        return {
            'id': self.id,
            'cpf': self.cpf,
            'birthday': self.birthday,
            'user_id': self.user_id
        }

class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    cnpj = Column(String(16), nullable=False, unique=True)
    description = Column(Text)
    address = Column(String(100), nullable=False)
    user_id = Column(Integer(), ForeignKey('users.id'))
    role = Column(PostgreSQLEnum(CompanyRole), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'cnpj': self.cnpj,
            'description': self.description,
            'address': self.address,
            'user_id': self.user_id,
            'role': self.role.value
        }


class Evaluation(Base):
    __tablename__ = "evaluations"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    person_id = Column(Integer(), ForeignKey('people.id'), unique=True)
    company_id = Column(Integer(), ForeignKey('companies.id'))
    comment = Column(Text)
    grade = (Column(Integer(), nullable=False))
    created_on = Column(DateTime(), default=datetime.now)

    def to_dict(self):
        return {
            'id': self.id,
            'person_id': self.person_id,
            'company_id': self.company_id,
            'comment': self.comment,
            'grade': self.grade,
            'created_on': self.created_on
        }