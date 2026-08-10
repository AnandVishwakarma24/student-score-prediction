import joblib
import pandas as pd

# Load the trained model saved in Day-10
model = joblib.load("Day-10/student_score_model.pkl")

# Simple CLI header
print("=" * 50)
print(f"\n Student Score Prediction System")
print("=" * 50)

# Collect user inputs for prediction features
hours = float(input("Enter Hours Studied: "))
attendance = float(input("Enter Attendance (%): "))
previous_score = float(input("Enter Previous Score: "))

# Prepare the input as a DataFrame for the model
student = pd.DataFrame({
    "Hours_Studied": [hours],
    "Attendance": [attendance],
    "Previous_Score": [previous_score]
})

# Run prediction and display result
prediction = model.predict(student)

print("\nPredicted Final Score:", round(prediction[0], 2))



