from flask import (
    Flask,
    render_template, 
    request
) 

import requests

app = Flask(__name__)

BACKEND_URL = "http://127.0.0.1:5004/notes"

@app.get("/")
@app.get("/notes")
def get_index():
    response = requests.get(BACKEND_URL)
    scan_data = response.json().get("notes")
    return render_template("main.html", notes=scan_data)

@app.route("/about")
def about():
    me = {
        "first_name": "Tim",
        "last_name": "Tom",
        "Hobbies": "DIY stuff and coding",
        "bio": "My name is Tim Tom, and I am student."
    }
    return render_template("about.html", about_dict = me)

# Createing a means to render a form
@app.get("/create/notes")
def create_notes_form():
    return render_template("new.html")

@app.post("/create/notes")
def create_notes():
    form_note = request.form
    new_note = {
        "title": form_note.get("title"),
        "subtitle": form_note.get("subtitle"),
        "body": form_note.get("body")
    }
    response = requests.post(BACKEND_URL, json=new_note)
    if response.status_code == 204:
        return render_template("new_success.html")
    else:
        return render_template("failed.html")

# Createing a means to render as update form
@app.get("/one/<int:pk>")
def view_one_note(pk):
    url = "%s/%s" % (BACKEND_URL, pk)
    response = requests.get(url)
    one_note = response.json().get("notes")
    return render_template("one_view.html", target_note=one_note[0])

# Createing a means to render as update form
@app.get("/<int:pk>")
def get_one_note(pk):
    url = "%s/%s" % (BACKEND_URL, pk)
    response = requests.get(url)
    update_note = response.json().get("notes")
    return render_template("update.html", target_note=update_note[0])

@app.post("/update/notes/<int:pk>")
def update_this_note(pk):
    form_note = request.form
    update_note = {
        "title": form_note.get("title"),
        "subtitle": form_note.get("subtitle"),
        "body": form_note.get("body")
    }
    url = "%s/%s" % (BACKEND_URL, pk)
    response = requests.put(url, json=update_note)
    if response.status_code == 204:
        return render_template("update_success.html")
    else:
        return render_template("update_fail.html")

@app.get("/delete/notes/<int:pk>")
def delete_this_note(pk):
    # response = requests.get(BACKEND_URL , str(pk))
    url = "%s/%s" % (BACKEND_URL, pk)
    response = requests.delete(url)
    if response.status_code == 204:
        return render_template("success_delete.html")
    else:
        return render_template("failed_delete.html")

 