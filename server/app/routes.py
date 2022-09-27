
from flask import (
    Flask,
    request
)

app = Flask(__name__)

from app.database import notes

RESPONSE = {
    "status": "ok",
}

@app.get("/notes")
def index():
    response = dict(RESPONSE)
    response["notes"] = notes.scan()
    return response

@app.get("/notes/<int:pk>")
def get_one(pk):
    response = dict(RESPONSE)
    response["notes"] = notes.select_by_id(pk)
    return response

@app.post("/notes")
def create_notes():
    nt_body = request.json
    notes.create(nt_body)
    return "", 204

@app.put("/notes/<int:pk>")
def update_notes(pk): # pk = primary key (_id column), because "id" is taken in python3
    up_nt_body = request.json
    notes.update(up_nt_body, pk)
    return "", 204

@app.delete("/notes/<int:pk>" )
def delete_notes(pk): # pk = primary key
    pk=str(pk)
    notes.delete(pk)
    return "", 204
