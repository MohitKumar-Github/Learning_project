from flask import Flask, request, jsonify
from datetime import date
from dateutil.relativedelta import relativedelta

app = Flask(__name__)

class BirthDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

@app.route("/health", methods=['GET'])
def api_run():
    return jsonify({"status": "success"})

@app.route('/calculate_age', methods=['POST'])
def calculate_age():
    data = request.json
    try:
        birth_date = BirthDate(day=data['day'], month=data['month'], year=data['year'])
        birth_date_obj = date(birth_date.year, birth_date.month, birth_date.day)
    except (ValueError, KeyError):
        return jsonify({"error": "Invalid date"}), 400

    today_date = date.today()
    age = relativedelta(today_date, birth_date_obj)

    return jsonify({
        "years": age.years,
        "months": age.months,
        "days": age.days
    })

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8002)