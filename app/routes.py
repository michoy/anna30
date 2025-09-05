from flask import Blueprint, request, render_template
import random

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template("home.html")

@main.route('/roll', methods=['POST'])
def roll():
    dice = random.randint(1, 30)
    if dice >= 15:
        heading = "Du slapp unna småprat!"
        message = f"Anna kaster en <b>{dice}</b>! Supert! Hun klarer elegant å unngå mer småprat.<br>" \
                  "Akkurat da dukker Sebastian overraskende opp med to mariokarter og utfordrer Anna til et kappløp til restauranten.<br>" \
                  "Godtar Anna utfordringen?"
    else:
        heading = "Mer småprat..."
        message = f"Anna kaster en <b>{dice}</b>. Ikke høyt nok! Den gamle damen fortsetter å prate om gamle Muay Thai dager.<br>" \
                  "Anna må holde ut med mer småprat til Sebastian endelig dukker opp med to mariokarter og utfordrer henne til et kappløp til restauranten.<br>" \
                  "Godtar Anna utfordringen?"
    return render_template("roll.html", heading=heading, message=message)

@main.route('/race', methods=['POST'])
def race():
    return render_template("race.html")

@main.route('/boost', methods=['POST'])
def boost():
    valg = request.form.get('valg')
    if valg == "krasj":
        resultat = "Anna kræsjer i Sebastian og får ett poeng! For et løp!"
    else:
        resultat = "Anna kjører rundt Sebastian for å bygge opp mer fart, men får ikke poeng denne gangen."
    return render_template("boost.html", resultat=resultat)
