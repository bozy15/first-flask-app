import os
import json
from flask import Flask, render_template, request, flash

if os.path.exists("env.py"): 
    import env

app = Flask(__name__)  # Standard Flask app
app.secret_key = os.environ.get('FLASK_SECRET_KEY') or 'secret-key' # Secret key for session management.

@app.route("/")  # Standard Flask app route
def index():
    return render_template("index.html")


@app.route("/about")  # Standard Flask app route
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:  # Open the JSON file for reading
        data = json.load(json_data)  # Read the JSON into the buffer
        for obj in data:  # Iterate over the list of dicts
            if obj["url"] == member_name:  # Find the member in the list
                member = obj  # Store the member's dict
    return render_template("member.html", member=member)  # And render the results


@app.route("/contact", methods=["GET", "POST"])  # Standard Flask app route
def contact():
    if request.method == "POST":  # If the form has been submitted...
        flash("Thanks {}, we have received your message!".format(request.form["name"]))  # Flash a message
    return render_template("contact.html", page_title="Contact Us")


@app.route("/careers")  # Standard Flask app route
def careers():
    return render_template("careers.html", page_title="Careers")


# run the app
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True,
    )
