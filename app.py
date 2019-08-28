# Import Dependencies 
from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import scrape_Mars
import os


# Create an instance of Flask app
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Route to render index.html template using data from Mongo
@app.route("/")
def index():

    # Find one record of data from the mongo database
    Mars_information = mongo.db.mars.find_one()

    # Return template and data
    return render_template("index.html", listings=Mars_information)

@app.route("/scrape")
def scrape():

    mars_db = mongo.db.Mars_information
    data = scrape_Mars.scrape()
    mars_db.update({},data,upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__": 
    app.run(debug= True)

