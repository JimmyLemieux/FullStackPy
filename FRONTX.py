from flask import Flask, render_template
from flask_restful import Api, Resource
from PARSECITYX import CITY_PARSE
from parseX import fetch_data


app = Flask(__name__)
api = Api(app)
CITIES=CITY_PARSE().PARSE()
RAW_LAWYER = fetch_data().GET('toronto')

class city_info(Resource):
    def get(self):
        CITIES["ATTENTION"] = "This Data is the sole property of LegalBase TM. You are free to request this data through any http requesting protocol you wish."
        return CITIES

class raw_lawyer_info(Resource):
    def get(self):
        CITIES["ATTENTION"] = "This Data is the sole property of LegalBase TM. You are free to request this data through any http requesting protocol you wish."
        return RAW_LAWYER

@app.route('/')
@app.route('/index.html')
def start():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

api.add_resource(city_info,'/city.json')
while __name__ == '__main__':
    app.run(debug=True,use_reloader=False)
