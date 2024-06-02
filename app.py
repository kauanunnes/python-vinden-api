from flask import Flask
from flask_restful import Api
from database.connection import db, engine
from models.models import Base
from controllers.user import Users, UserById, People, Companies, Evaluations

Base.metadata.create_all(engine)

app = Flask(__name__)
api = Api(app)

api.add_resource(Users, '/users') 
api.add_resource(UserById, '/users/<id>') 
api.add_resource(People, '/people') 
api.add_resource(Companies, '/companies') 
api.add_resource(Evaluations, '/evaluations') 

if __name__ == '__main__':
    app.run(debug=True)