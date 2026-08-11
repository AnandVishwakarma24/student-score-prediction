from flask import Flask, render_template, request
import joblib
import pandas as pd
import os

# Reduce memory usage by limiting numerical library threads
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"

from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

app = Flask(__name__)

# Get the Day-11 folder location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load trained model from Day-10
model_path = os.path.join(
    BASE_DIR,
    "..",
    "Day-10",
    "student_score_model.pkl"
)

model = joblib.load(model_path)


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None

    if request.method == "POST":

        hours = float(request.form["hours"])
        attendance = float(request.form["attendance"])
        previous_score = float(request.form["previous_score"])

        student = pd.DataFrame({
            "Hours_Studied": [hours],
            "Attendance": [attendance],
            "Previous_Score": [previous_score]
        })

        # Make prediction
        prediction = model.predict(student)[0]

        # Keep prediction between 0 and 100
        prediction = max(0, min(100, prediction))

        # Round to 2 decimal places
        prediction = round(prediction, 2)

    return render_template(
        "index.html",
        prediction=prediction
    )


if __name__ == "__main__":
    app.run(debug=True)