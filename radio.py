from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Chargement des stations depuis un fichier JSON
with open('stations.json') as f:
    stations = json.load(f)['stations']

@app.route('/')
def index():
    return render_template('index.html', stations=stations)

@app.route('/station/<int:station_id>')
def station(station_id):
    station = stations[station_id]
    return render_template('station.html', station=station)

if __name__ == '__main__':
    # Rendre l'application accessible sur tout le réseau local
    app.run(host='0.0.0.0', port=5000, debug=True)
