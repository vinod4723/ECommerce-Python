import os
from fastapi import FastAPI
from contextlib import asynccontextmanager

from flask import Flask
basedir = os.path.abspath(os.path.dirname(__file__))

from db.session import engine
from models.product import Product
from db.base_class import Base


app = Flask(__name__)
# Create the database tables
Base.metadata.create_all(bind=engine)
@app.route('/')
def index():
    return "Welcome to the E-Commerce API!"
