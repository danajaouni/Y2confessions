from models import Base, Confession
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///person.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_Confession(message, hub):
	confession_object = Confession(
	message=message,hub=hub)
	session.add(confession_object)
	session.commit()

def delete_Confession(id):
  session.query(Confession).filter_by(id = id).delete()
  session.commit()
