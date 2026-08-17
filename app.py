from flask import Flask, request, render_template
from database import initialize_database, add_student

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


# Initialize database when application starts
initialize_database()


# Home route
@app.route("/")
def home():
    return render_template("index.html")


# Student result route
@app.route("/result", methods=["POST"])
def student_result():

    name = request.form["name"]

    marks1 = int(request.form["marks1"])
    marks2 = int(request.form["marks2"])
    marks3 = int(request.form["marks3"])

    marks = [marks1, marks2, marks3]

    total = calculate_total(marks)
    average = calculate_average(marks)
    result = calculate_result(marks)

    # Store result in SQLite database
    add_student(
        name,
        marks1,
        marks2,
        marks3,
        total,
        result
    )

    return render_template(
        "index.html",
        name=name,
        total=total,
        average=average,
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)