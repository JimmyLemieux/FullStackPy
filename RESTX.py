from flask import Flask
from flask_restful import Api, Resource
from parseX import fetch_data

app = Flask(__name__)
api = Api(app)

a = fetch_data()
OUT = a.GET('Toronto', 3)

class out_info(Resource):
    def get(self):
        return OUT


api.add_resource(out_info,'/')

if __name__ == '__main__':
    app.run(debug=True,use_reloader=False)
