# Import Dependencies 
from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import scrape_Mars
import os


# Create an instance of Flask app
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
#mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# conn = "mongodb://localhost:27017/mars_app"
# client = pymongo.MongoClient(conn)

# db = client.mars_info
# collection = db.mars

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/craigslist_app"
mongo = PyMongo(app)

@app.route("/scrape")
def scrape():

    # mars_db = mongo.db.Mars_information
    # data = scrape_Mars.scrape()
    # mars_db.update({},data,upsert=True)
    # return redirect("/", code=302)

    listings = mongo.db.listings
    listings_data = scrape_Mars.scrape()
    listings.update({}, listings_data, upsert=True)
    return redirect("/", code=302)



# Route to render index.html template using data from Mongo
@app.route("/")
def index():

    # # Find one record of data from the mongo database
    # Mars_information = list(db.collection.find())
    # print(Mars_information)

    # # Return template and data
    # return render_template("index.html", listings=Mars_information)

    listings = mongo.db.listings.find_one()
    return render_template("index.html", listings=listings)

if __name__ == "__main__": 
    app.run(debug= True)

