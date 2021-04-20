from flask import Flask, render_template
import pymongo
import mission_to_mars

app = Flask(__name__)

conn= 'mongodb://localhost:27017/'
client = pymongo.MongoClient(conn)

db=client.mars_db

@app.route("/")
def index():
    mars = mongo.db.mars_db.find_one()
    return render_template("index.html", mars=mars)


@app.route("/scrape")
def scrapper():
    mars = mongo.db.mars_db
    mars_data = mission_to_mars.scrape_all()
    mars.update({}, mars_data, upsert=True)
    return "Scraping Done"


if __name__ == "__main__":
    app.run()