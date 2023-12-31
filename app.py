from flask import Flask, request
import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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
    url = request.form.get("url")
    return db.rooms_create(name, city, state, url)


@app.route("/rooms/<id>.json")
def show(id):
    return db.rooms_find_by_id(id)


@app.route("/rooms/<id>.json", methods=["PATCH"])
def update(id):
    name = request.form.get("name")
    city = request.form.get("city")
    state = request.form.get("state")
    url = request.form.get("url")
    return db.rooms_update_by_id(id, name, city, state, url)


@app.route("/rooms/<id>.json", methods=["DELETE"])
def destroy(id):
    return db.rooms_destroy_by_id(id)