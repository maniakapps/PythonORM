"""Database config."""
#  __Author__= "Manuel Pizano"
#  __Email__= "doomclass@proton.me"
#  __Website__= "https://github.com/maniakapps"
#  __Portfolio__= "https://portafoliofullstack.vercel.app/"
#
#  Copyright (c) 2022.

from os import environ, path

from dotenv import load_dotenv

# Load variables from enviroment system
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

# Database connection variables
SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_DATABASE_PEM = environ.get("SQLALCHEMY_DATABASE_PEM")

# Reset data after each run
CLEANUP_DATA = False
