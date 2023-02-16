
from flask import Flask, jsonify, render_template
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import psycopg2
import json

engine = create_engine('postgresql://postgres:postgres@localhost:5432/Malaysia')

Base = automap_base()
Base.prepare(engine, reflect=True)

Roadacc = Base.classes.road_accidents



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ProcessUserinfo/<string:userinfo>', methods=['POST'])
def ProcessUserinfo(userinfo):
    userinfo = json.loads(userinfo)
    username = userinfo
    print('-----')
    print(f"Your name is {username}")
    print('-----')
    return('/')

@app.route('/accidents')
def accidents():
    session = Session(engine)
    data = session.query(Roadacc.road_crashes, Roadacc.population, Roadacc.year).all()
    session.close()

    results = [{"Crashes": r.road_crashes, "Population": r.population, "Year": r.year} for r in data]

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/testquery/<startyear>')
def getYear(start):
    year = int(start)
    session = Session(engine)
    data = session.query(Roadacc.road_crashes, Roadacc.year).filter(Roadacc.year > year).all()
    session.close()
    results = [{"Crashes": r.road_crashes, "Year": r.year} for r in data]
    return jsonify(results)