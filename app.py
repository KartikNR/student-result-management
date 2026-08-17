from flask import Flask, request, jsonify

app = Flask(__name__)


# Calculate total marks
def calculate_total(marks):
    return sum(marks)


# Calculate average marks
def calculate_average(marks):
    return sum(marks) / len(marks)


# Determine result
def calculate_result(marks):
    average = calculate_average(marks)

    if average >= 40:
        return "PASS"
    else:
        return "FAIL"


# Home route
@app.route("/")
def home():
    return "Student Result Management Backend"


# Student result route
@app.route("/result", methods=["POST"])
def student_result():

    data = request.get_json()

    name = data["name"]
    usn = data["usn"]
    marks = data["marks"]

    total = calculate_total(marks)
    average = calculate_average(marks)
    result = calculate_result(marks)

    return jsonify({
        "name": name,
        "usn": usn,
        "marks": marks,
        "total": total,
        "average": average,
        "result": result
    })


if __name__ == "__main__":
    app.run(debug=True)