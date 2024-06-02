from flask import request, jsonify
from flask_restful import Resource
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from json import dumps
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.connection import engine
from models.models import User, Person, Company, CompanyRole, Evaluation

Session = sessionmaker(bind=engine)
session = Session()


class Users(Resource):
    def get(self):
        users = session.query(User).all()
        return jsonify([user.to_dict() for user in users])

    def post(self):
        name = request.json['name']
        email = request.json['email']
        login = request.json['login']
        password = request.json['password']
        phone = request.json['phone']

        new_user = User(name=name, email=email, login=login, password=password, phone=phone)

        session.add(new_user)
        
        session.commit()

        users = session.query(User).all()
        
        return jsonify([user.to_dict() for user in users])
    

class UserById(Resource):
    def get(self, id):
      user = session.query(User).filter_by(id=id).first()
      if user:
          return jsonify(user.to_dict())
      else:
          return jsonify({'error': 'User not found'}), 404
      
    def delete(self, id):
        user = session.query(User).filter_by(id=id).first()

        if user:
            session.delete(user)
            session.commit()
            response = jsonify({'message': 'User deleted successfully'})
            response.status_code = 200
        else:
            response = jsonify({'error': 'User not found'})
            response.status_code = 404
        return response
    
class People(Resource):
    def get(self):
      people = session.query(Person).all()
      return jsonify([person.to_dict() for person in people])
    
    def post(self):
        name = request.json['name']
        email = request.json['email']
        login = request.json['login']
        password = request.json['password']
        phone = request.json['phone']

        new_user = User(name=name, email=email, login=login, password=password, phone=phone)

        session.add(new_user)
        session.flush()

        if new_user:
          cpf = request.json['cpf']
          birthday = request.json['birthday']
          user_id = new_user.id
          new_person = Person(cpf=cpf, birthday=birthday, user_id=user_id)

          session.add(new_person)
          
          session.commit()

        people = session.query(Person).all()
        
        return jsonify([person.to_dict() for person in people])
    
class Companies(Resource):
    def get(self):
      companies = session.query(Company).all()
      return jsonify([company.to_dict() for company in companies])
    
    def post(self):
      name = request.json['name']
      email = request.json['email']
      login = request.json['login']
      password = request.json['password']
      phone = request.json['phone']

      new_user = User(name=name, email=email, login=login, password=password, phone=phone)

      session.add(new_user)
      session.flush()

      if new_user:
          cnpj = request.json['cnpj']
          description = request.json['description']
          address = request.json['address']
          role = CompanyRole[request.json['role']]
          user_id = new_user.id
          new_company = Company(cnpj=cnpj, description=description, address=address, role=role, user_id=user_id)

          session.add(new_company)
          
          session.commit()

      companies = session.query(Company).all()
      
      return jsonify([company.to_dict() for company in companies])
    
class Evaluations(Resource):
    def get(self):
        evaluations = session.query(Evaluation).all()
        return jsonify([evaluation.to_dict() for evaluation in evaluations])
    
    def post(self):
        person_id = request.json['person_id']
        company_id = request.json['company_id']
        grade = request.json['grade']
        comment = request.json['comment']
        evaluation = Evaluation(person_id=person_id, company_id=company_id, grade=grade, comment=comment)
        session.add(evaluation)
        session.commit()

        return jsonify(evaluation.to_dict())