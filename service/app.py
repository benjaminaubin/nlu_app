from os import name
from flask import Flask, request, jsonify, make_response
import flask
from flask_restplus import Api, Resource, fields
import joblib

flask_app = Flask(__name__)
app = Api(
    app=flask_app,
    version="1.0.0",
    title="Natural Langage Understanding",
    description=""
)

name_space = app.namespace('prediction', description='Prediction APIs')

model = app.model(
    'Prediction params',
    {'sentence': fields.Float(
        required=True,
        description="Sentence",
        help="Sentence cannot be blank")
     }
)

model_intent = joblib.load("nlu/model_intent.joblib")


@name_space.route("/")
class MainClass(Resource):

    def options(self):
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add('Access-Control-Allow-Headers', "*")
        response.headers.add('Access-Control-Allow-Methods', "*")
        return response

    @app.expect(model)
    def post(self):
        try:
            formData = request.json
            sentence = formData["sentence"]
            prediction = model_intent.predict([sentence])
            print(prediction)
            types = {
                0: "AddToPlaylist", 1: "BookRestaurant", 2: "GetWeather",
                3: "PlayMusic", 4: "RateBook", 5: "SearchCreativeWork",
                6: "SearchScreeningEvent"
            }
            response = jsonify({
                "statusCode": 200,
                "status": "Prediction made",
                "result": "" + types[prediction[0]]
            })
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response

        except Exception as error:
            return jsonify({
                "statusCode": 500,
                "status": "Could not make prediction",
                "error": str(error)
            })
