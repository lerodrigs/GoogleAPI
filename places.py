from flask import Flask, render_template, jsonify, request
import requests
from key import key 
import imghdr

app = Flask(__name__)

search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
search_geo = "https://www.googleapis.com/geolocation/v1/geolocate"
search_reverse_geo = "https://maps.googleapis.com/maps/api/geocode/json"

@app.route("/", methods = ["GET"])
def retreive():
  return render_template('layout.html')

@app.route("/sendRequest/<string:query>")
def results(query):
    search_payload = {"key": key,"query": query}
    search_req = requests.get(search_url, params=search_payload)
    search_json = search_req.json()

    return search_json

@app.route("/getGeolocate")
def getGeolocate():
    search_req = requests.post(search_geo + "?key=" + key)
    search_json = search_req.json()
    latitude = search_json["location"]["lat"]
    lat = str(latitude)

    longitude = search_json["location"]["lng"]
    lng = str(longitude)
    print(lat,lng)
    search_req2 = requests.get(search_reverse_geo + "?latlng=" + lat + "," + lng + "&key=" + key)

    resp = search_req2.json()

    return resp

if __name__ == "__main__":
  app.run(debug = True)