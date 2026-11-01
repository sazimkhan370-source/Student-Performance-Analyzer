from flask import Flask, render_template, request
from model import predict_performance

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        roll_number = request.form.get("roll_number", "").strip()
        subjects = ["English", "Mathematics", "Computer", "Science", "Hindi"]

        try:
            marks = [float(request.form.get(subject, "")) for subject in subjects]
        except (TypeError, ValueError):
            return render_template("index.html", error="Please enter marks for all five subjects.")

        if not name or not roll_number:
            return render_template("index.html", error="Please enter the student's name and roll number.")

        if any(mark < 0 or mark > 100 for mark in marks):
            return render_template("index.html", error="Marks must be between 0 and 100.")

        total = sum(marks)
        percentage = total / len(marks)
        prediction = predict_performance(marks)

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 40:
            grade = "D"
        else:
            grade = "F"

        return render_template(
            "result.html",
            name=name,
            roll_number=roll_number,
            subjects=subjects,
            marks=marks,
            total=total,
            percentage=percentage,
            grade=grade,
            prediction=prediction
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
