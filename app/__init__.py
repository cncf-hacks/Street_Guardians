from flask import Flask, render_template, request
from geopy.geocoders import Nominatim
import folium

marker_locations = []

app = Flask(__name__, template_folder='templates')
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/home", methods=["GET"])
def home():
    return render_template('home.html')

@app.route("/report", methods=["GET"])
def report():
    return render_template('report-input.html')

@app.route("/submit_data", methods=["POST"])
def submit_data():
    severity = request.form['severity']
    title = request.form['title']
    description = request.form['description']
    address = request.form['address']

    process_data(severity, description, title, address)
    return render_template('thank-you.html')


@app.route("/map", methods=["GET"])
def event_mapper():
    m = render_map(marker_locations)
    map_html = m.get_root().render()
    return render_template('map.html', map_html=map_html)

def process_data(severity: str, description: str, title: str, address: str) -> list:
    geolocator = Nominatim(user_agent="my_geocoder")
    location = geolocator.geocode(address)
    marker_locations.append(
        {
            "location": [location.latitude, location.longitude],
            "description": description,
            "title": title,
            "severity": severity,
            "address": address
        })
    return [location.latitude, location.longitude]


def render_map(marker_locations):
    m = folium.Map(location=(5.543367, -73.361205), zoom_start=15, tiles="stadia alidadesmoothdark")

    for marker in marker_locations:
        location = marker["location"]
        title = marker["title"]
        description = marker["description"]
        severity = marker["severity"]
    
        icon_color = "blue"
        if severity == "high":
            icon_color = "red"
        elif severity == "medium":
            icon_color = "orange"

        folium.Marker(
              location=location,
              tooltip=title,
              popup=description,
              icon=folium.Icon(icon="glyphicon glyphicon-plus", color=icon_color)
         ).add_to(m)

    return m

if __name__ == "__main__":
    app.run(debug=True)


