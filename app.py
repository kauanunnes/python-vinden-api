from flask import Flask
from flask_restful import Api
from database.connection import db, engine
from flask_cors import CORS
from models.models import Base
from controllers.user import Users, UserById, People, Companies, Evaluations

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

Base.metadata.create_all(engine)

app = Flask(__name__)
api = Api(app)
CORS(app)
api.add_resource(Users, '/users') 
api.add_resource(UserById, '/users/<id>') 
api.add_resource(People, '/people') 
api.add_resource(Companies, '/companies') 
api.add_resource(Evaluations, '/evaluations') 


@app.route("/")
def helloWorld():
  return "Hello, cross-origin-world!"

if __name__ == '__main__':
    app.run(debug=True)

