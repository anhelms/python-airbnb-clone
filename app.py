from flask import Flask, request
import db

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route("/rooms.json")
def index():
    return db.rooms_all()


@app.route("/rooms.json", methods=["POST"])
def create():
    name = request.form.get("name")
    city = request.form.get("city")
    state = request.form.get("state")
    return db.rooms_create(name, city, state)


@app.route("/rooms/<id>.json")
def show(id):
    return db.rooms_find_by_id(id)