"""Create SQLAlchemy engine and session objects."""
#  __Author__= "Manuel Pizano"
#  __Email__= "doomclass@proton.me"
#  __Website__= "https://github.com/maniakapps"
#  __Portfolio__= "https://portafoliofullstack.vercel.app/"
#
#  Copyright (c) 2022.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import SQLALCHEMY_DATABASE_PEM, SQLALCHEMY_DATABASE_URI

# Create database engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URI, connect_args={"ssl": {"key": SQLALCHEMY_DATABASE_PEM}}
)
# engine = create_engine('postgresql://postgres:1234@localhost:5432/Airport')
# Create database session
Session = sessionmaker(bind=engine)
session = Session()
