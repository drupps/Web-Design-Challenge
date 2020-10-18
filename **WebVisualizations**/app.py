# 1. import Flask
from flask import Flask, jsonify

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


@app.route("/")
def index():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/"
        f"/api/v1.0/viz1<br/>"
        f"/api/v1.0/viz2<br/>"
        f"/api/v1.0/viz3<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )



# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Welcome to my 'Home' page!"


# 4. Define what to do when a user hits the /about route
@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"


if __name__ == "__main__":
    app.run(debug=True)
