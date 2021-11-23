from flask import Flask, Response, request
from src.domain.user import User
from src.domain.insurance import Insurance
from flask_expects_json import expects_json

app = Flask(__name__)

schema = {
  "type": "object",
  "properties": {
    "age": { "type": "number"},
    "dependents": { "type": "number" },
    "income": { "type": "number" },
    "house": { "type": "object" , "properties": { "ownership_status": {"type": "string"} }},
    "marital_status": { "type": "string", "enum": ["married", "single"]},
    "risk_questions": { "type": "array", "minLength": 3, "maxLenght": 3 },
    "vehicle": {"type": "object", "properties": {"year": {"type": "number"}}},
  },
  "required": ["age", "dependents", "income", "risk_questions", "marital_status"]
}

@app.route('/', methods=['POST'])
@expects_json(schema)
def post():
    age = request.json['age']
    dependents = request.json['dependents']
    house = request.json['house']['ownership_status']
    income = request.json['income']
    marital_status = request.json['marital_status']
    risk_questions = request.json['risk_questions']
    vehicle = request.json['vehicle']['year']

    user = User(age, dependents, house, income, marital_status, risk_questions, vehicle)
    insurance = Insurance(user)
    score = insurance.get_risk_score()

    return score


if __name__ == '__main__':
    app.run(debug=True)
