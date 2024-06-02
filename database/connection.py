from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy.engine import URL
import os

load_dotenv()

url = URL.create(
    drivername="postgresql",
    username=os.environ['USER'],
    host=os.environ['HOST'],
    database=os.environ['DATABASE'],
    password=os.environ['PASSWORD'],
    port=os.environ['PORT']
)

engine = create_engine(url)

db = engine.connect()
