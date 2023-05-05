"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaagk2k728r886hkq80-a.oregon-postgres.render.com/todo_2xh3",
        database="todo_2xh3",
        user="todo_2xh3_user",
        password="T29sKtf4VrI1C0y6K3AfUzM81Zn30cwh")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
