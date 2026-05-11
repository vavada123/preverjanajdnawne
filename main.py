from flask import Flask, render_template, request
from tinydb import TinyDB
import requests

db = TinyDB('iskanje.json')

app = Flask(__name__)

@app.route("/Nation")
def Nation():
    
    return render_template("nation.html")

@app.route("/NationData")
def NationData():
    drzava = request.args.get('drzava')

    url = f"https://api.nationalize.io/?name={drzava}"
    response = requests.get(url)
    podatki = response.json()

    prvadrzava = podatki.get('country', [])
    prvadrzavaid = prvadrzava[0].get('country_id')

    ime = request.args.get('ime')
    email = request.args.get('email')
    geslo = request.args.get('geslo')

    print(ime, email, geslo)

    db.insert({"ime" : ime, "email" : email, "geslo" : geslo, "drzava" : drzava})

    if drzava == prvadrzavaid:
        return {"status" : "Uspesno"}

        

app.run(debug = True)