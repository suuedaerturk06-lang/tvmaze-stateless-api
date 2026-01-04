from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

TVMAZE_BASE = "https://api.tvmaze.com"

@app.route("/")
def home():
    return render_template("index.html")

# HTML üzerinden arama
@app.route("/search")
def search_html():
    query = request.args.get("q")
    if not query:
        return render_template("index.html")

    r = requests.get(f"{TVMAZE_BASE}/search/shows?q={query}")
    return render_template("index.html", results=r.json())

# JSON API (stateless)
@app.route("/api/search/<query>")
def search_api(query):
    r = requests.get(f"{TVMAZE_BASE}/search/shows?q={query}")
    return jsonify(r.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
