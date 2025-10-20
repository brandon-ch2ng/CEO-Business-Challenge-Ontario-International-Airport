from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def parking():
    lots = [
    {
        "name": "Lot 2 General",
        "available": 460,
        "total": 1219,
        "percent_full": 62,
        "reserve_url": "https://booking.flyontario.com/en/",
        # NEW FIELDS
        "address": "Lot 2, Terminal Way, Ontario, CA 91761",
        "map_url": "https://maps.app.goo.gl/jTK6rEdnn9XBFGQt7",
        "about": "Directly in front of Terminal 2. Rates start at $10.00 for 1 hr.",
        "features": [
            "EV charging station available"
        ],
        "pricing": [
            {"label": "Up to 1 hour", "price": "$10"},
            {"label": "Up to 2 hours", "price": "$15"},
            {"label": "Up to 24 hours", "price": "$30"},
            {"label": "Additional Days", "price": "$30/day"}
        ],
        "image_url": url_for('static', filename='lots/lot2general.png'),
    },
    {
        "name": "Lot 2 Premium",
        "available": 32,
        "total": 324,
        "percent_full": 90,
        "reserve_url": "https://booking.flyontario.com/en/",
        # NEW FIELDS
        "address": "Lot 2, Terminal Way, Ontario, CA 91761",
        "map_url": "https://maps.app.goo.gl/jTK6rEdnn9XBFGQt7",
        "about": "A shorter walk to Terminal 2. Rates start at $12.00 for 1 hr.",
        "features": [
            "EV charging station available"
        ],
        "pricing": [
            {"label": "Up to 1 hour", "price": "$12"},
            {"label": "Up to 2 hours", "price": "$18"},
            {"label": "Up to 24 hours", "price": "$35"},
            {"label": "Additional Days", "price": "$35/day"}
        ],
        "image_url": url_for('static', filename='lots/lot2premium.png'),
    },
    {
        "name": "Lot 3",
        "available": 477,
        "total": 1192,
        "percent_full": 60,
        "reserve_url": "https://booking.flyontario.com/en/",
        # NEW FIELDS
        "address": "Lot 3, Ontario, CA 91761",
        "map_url": "https://maps.app.goo.gl/b5w2dvttAx5q4kWc8",
        "about": "In between Terminal 2 and 4. A short walk from both. Full day parking at $25.00 per day.",
        "pricing": [
            {"label": "Up to 24 hours", "price": "$25"},
            {"label": "Additional Days", "price": "$25/day"}
        ],
        "image_url": url_for('static', filename='lots/lot3.png'),
    },
    {
        "name": "Lot 4 General",
        "available": 1028,
        "total": 1430,
        "percent_full": 29,
        "reserve_url": "https://booking.flyontario.com/en/",
        # NEW FIELDS
        "address": "ONT - Lot 4, E Terminal Wy, Ontario, CA 91761",
        "map_url": "https://maps.app.goo.gl/ijcLSTqxaeyYGLi66",
        "about": "Directly in front of Terminal 4. Rates start at $10.00 for 1 hr.",
        "features": [
            "EV charging station available"
        ],
        "pricing": [
            {"label": "Up to 1 hour", "price": "$10"},
            {"label": "Up to 2 hours", "price": "$15"},
            {"label": "Up to 24 hours", "price": "$30"},
            {"label": "Additional Days", "price": "$30/day"}
        ],
        "image_url": url_for('static', filename='lots/lot4general.png'),
    },
    {
        "name": "Lot 4 Premium",
        "available": 25,
        "total": 352,
        "percent_full": 93,
        "reserve_url": "https://booking.flyontario.com/en/",
        # NEW FIELDS
        "address": "ONT - Lot 4 Premium Parking, E Terminal Wy, Ontario, CA 91761",
        "map_url": "https://maps.app.goo.gl/MAewTEu4TBzMqXJe8",
        "about": "A shorter walk to Terminals 4. Rates start at $12.00 for 1 hr.",
        "features": [
            "EV charging station available"
        ],
        "pricing": [
            {"label": "Up to 1 hour", "price": "$12"},
            {"label": "Up to 2 hours", "price": "$18"},
            {"label": "Up to 24 hours", "price": "$35"},
            {"label": "Additional Days", "price": "$35/day"}
        ],
        "image_url": url_for('static', filename='lots/lot4premium.png'),
    },
    {
        "name": "Lot 5",
        "available": 1172,
        "total": 2200,
        "percent_full": 47,
        "reserve_url": "https://maps.app.goo.gl/2i5ZBA5hYiXYEJbG9",
        # NEW FIELDS
        "address": "Parking lot5 Ontario, CA 91761",
        "map_url": "https://maps.google.com/?q=2500+E+Airport+Dr+Ontario+CA+91761",
        "about": "Great value parking and shuttle service provided. Short walk to Terminal 4. Full-day parking at $20.00 per day.",
        "features": [
            "This is a cashless lot. Only credit cards will be accepted for payment."
        ],
        "pricing": [
            {"label": "Up to 24 hours", "price": "$20"},
            {"label": "Additional Days", "price": "$20/day"}
        ],
        "image_url": url_for('static', filename='lots/lot5.png'),
    },
    {
        "name": "Lot 6",
        "available": 839,
        "total": 1337,
        "percent_full": 37,
        "reserve_url": "https://booking.flyontario.com/en/",
        # NEW FIELDS
        "address": "Lot 6, Ontario International Airport, Cell Phone Waiting Lot, John Bangs Dr, Ontario, CA 91761",
        "map_url": "https://maps.app.goo.gl/4r36jGAbKpCo7QvU8",
        "about": "Great value parking and shuttle service provided. Short walk to Terminal 4. Full-day parking at $20.00 per day.",
        "features": [
            "This is a cashless lot. Only credit cards will be accepted for payment."
        ],
        "pricing": [
            {"label": "Up to 24 hours", "price": "$20"},
            {"label": "Additional Days", "price": "$20/day"}
        ],
        "image_url": url_for('static', filename='lots/lot6.png'),
    },
]
    return render_template("index.html", lots=lots)

@app.route("/shuttle")
def shuttle():
    return render_template("shuttle.html")

if __name__ == "__main__":
    app.run(debug=True)
