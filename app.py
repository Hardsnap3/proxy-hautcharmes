from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/brive-agenda')
def brive_agenda():
    url = "https://www.brive.fr/agenda/complet"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    # Sélectionne les blocs d'événements
    events = []
    # Trouve tous les blocs événements (structure du site au 08/06/2025)
    for card in soup.select(".card-event"):
        titre = card.select_one(".card-title")
        date = card.select_one(".date-badge")
        desc = card.select_one(".card-text")
        lien = card.select_one("a")
        events.append({
            "titre": titre.text.strip() if titre else "",
            "date": date.text.strip() if date else "",
            "desc": desc.text.strip() if desc else "",
            "url": lien["href"] if lien else ""
        })
        if len(events) >= 7:  # Prends les 7 premiers
            break
    return jsonify(events)

@app.route('/')
def hello():
    return "Proxy Agenda Brive OK !"

if __name__ == '__main__':
    app.run()
