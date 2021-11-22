from flask import Flask, Response, request
from src.domain.user import User
from src.domain.insurance import Insurance

app = Flask(__name__)


@app.route('/', methods=['POST'])
def post():
    age = request.json['age']
    dependents = request.json['dependents']
    house = request.json['house']
    income = request.json['income']
    marital_status = request.json['marital_status']
    risk_questions = request.json['risk_questions']
    vehicle = request.json['vehicle']

    user = User(age, dependents, house, income, marital_status, risk_questions, vehicle)
    insurance = Insurance(user)
    score = insurance.get_risk_score()

    return score


if __name__ == '__main__':
    app.run(debug=True)
