from flask import Flask, render_template, jsonify

app = Flask(__name__)


# -------------------------------------------------
# DISASTER DATA
# -------------------------------------------------

disasters = {
    "Earthquake": {
        "image": "earthquake.jpg",
        "description": "An earthquake is sudden ground shaking caused by movement beneath the Earth's surface.",
        "tips": [
            "Stay calm and do not panic.",
            "Drop, Cover and Hold.",
            "Stay away from windows and heavy objects.",
            "Do not use elevators.",
            "After shaking stops, move to a safe open area."
        ]
    },

    "Flood": {
        "image": "flood.jpg",
        "description": "A flood happens when water covers normally dry land due to heavy rainfall, rivers or storms.",
        "tips": [
            "Move to higher ground.",
            "Never walk or drive through flood water.",
            "Keep emergency supplies ready.",
            "Switch off electricity if it is safe.",
            "Follow official warnings."
        ]
    },

    "Fire": {
        "image": "fire.jpg",
        "description": "Fire can spread quickly and produce dangerous smoke and heat.",
        "tips": [
            "Raise the alarm immediately.",
            "Use stairs instead of elevators.",
            "Stay low if there is smoke.",
            "Do not go back inside a burning building.",
            "Call emergency services."
        ]
    },

    "Cyclone": {
        "image": "cyclone.jpg",
        "description": "A cyclone is a powerful storm with strong winds and heavy rainfall.",
        "tips": [
            "Stay indoors.",
            "Keep doors and windows closed.",
            "Keep emergency supplies ready.",
            "Stay away from windows.",
            "Follow official weather warnings."
        ]
    }
}


# -------------------------------------------------
# HOME
# -------------------------------------------------

@app.route("/")
def home():
    return render_template("home.html")


# -------------------------------------------------
# DISASTERS
# -------------------------------------------------

@app.route("/disasters")
def disaster_page():
    return render_template(
        "disasters.html",
        disasters=disasters
    )


# -------------------------------------------------
# INDIVIDUAL DISASTER PAGES
# -------------------------------------------------

@app.route("/earthquake")
def earthquake():
    return render_template(
        "earthquake.html",
        disaster=disasters["Earthquake"]
    )


@app.route("/flood")
def flood():
    return render_template(
        "flood.html",
        disaster=disasters["Flood"]
    )


@app.route("/fire")
def fire():
    return render_template(
        "fire.html",
        disaster=disasters["Fire"]
    )


@app.route("/cyclone")
def cyclone():
    return render_template(
        "cyclone.html",
        disaster=disasters["Cyclone"]
    )


# -------------------------------------------------
# CHECKLIST
# -------------------------------------------------

@app.route("/checklist")
def checklist():
    return render_template("checklist.html")


# -------------------------------------------------
# EMERGENCY
# -------------------------------------------------

@app.route("/emergency")
def emergency():
    return render_template("emergency.html")


# -------------------------------------------------
# ABOUT
# -------------------------------------------------

@app.route("/about")
def about():
    return render_template("about.html")


# -------------------------------------------------
# API
# -------------------------------------------------

@app.route("/api/<disaster>")
def disaster_api(disaster):

    data = disasters.get(disaster)

    if data:
        return jsonify(data)

    return jsonify({
        "error": "Disaster information not found"
    })


# -------------------------------------------------
# RUN
# -------------------------------------------------


if __name__ == "__main__":
    print("RUNNING FROM:", app.root_path)
    app.run(debug=True)