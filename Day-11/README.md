# Day-11: Student Score Prediction Web App

## 📌 Project Overview

This project converts the **Student Score Prediction Machine Learning model** developed in Day-10 into a web application using **Flask**.

The application provides a simple web interface where users can enter:

* Hours Studied
* Attendance
* Previous Score

The trained Machine Learning model then predicts the student's **Final Score**.

---

## 🎯 Objective

The main objective of Day-11 is to learn how to:

* Integrate a trained Machine Learning model with Flask
* Create a web interface for ML predictions
* Accept user input through an HTML form
* Send input data to a trained model
* Display the predicted result on a webpage
* Organize Flask project files properly

---

## 🛠️ Technologies Used

* **Python**
* **Flask** – Web application framework
* **Pandas** – Data preparation
* **Joblib** – Loading the trained ML model
* **Scikit-learn** – Machine Learning model
* **HTML/CSS** – Frontend interface

---

## 📂 Project Structure

```text
Student-Score-Prediction/
│
├── Day-10/
│   └── student_score_model.pkl
│
├── Day-11/
│   ├── app.py
│   ├── README.md
│   │
│   └── templates/
│       └── index.html
│
└── ...
```

The trained model from **Day-10** is loaded by the Flask application from:

```text
../Day-10/student_score_model.pkl
```

---

## ⚙️ How the Application Works

The application follows this workflow:

```text
User Input
    ↓
Flask Web Form
    ↓
Convert Input to Numbers
    ↓
Create Pandas DataFrame
    ↓
Load Trained ML Model
    ↓
Generate Prediction
    ↓
Limit Score Between 0–100
    ↓
Round Prediction to 2 Decimal Places
    ↓
Display Result
```

---

## 📊 Input Features

The model uses three features for prediction:

| Feature          | Description                   |
| ---------------- | ----------------------------- |
| `Hours_Studied`  | Number of hours studied       |
| `Attendance`     | Student attendance percentage |
| `Previous_Score` | Previous examination score    |

### Target

```text
Final_Score
```

---

## 🧠 Model Integration

The trained model is loaded using Joblib:

```python
model = joblib.load(model_path)
```

User input is converted into a Pandas DataFrame with the same feature names used during model training:

```python
student = pd.DataFrame({
    "Hours_Studied": [hours],
    "Attendance": [attendance],
    "Previous_Score": [previous_score]
})
```

The model then generates the prediction:

```python
prediction = model.predict(student)[0]
```

---

## 📈 Prediction Processing

The prediction is restricted to a valid score range of **0 to 100**:

```python
prediction = max(0, min(100, prediction))
```

The final result is rounded to two decimal places:

```python
prediction = round(prediction, 2)
```

For example:

```text
Predicted Final Score: 87.45
```

---

## 🌐 Flask Application

The application uses the following route:

```python
@app.route("/", methods=["GET", "POST"])
```

### GET Request

Displays the prediction form.

### POST Request

Receives the user's input, sends it to the trained model, and displays the prediction.

---

## 🚀 Installation

Make sure Python is installed on your system.

Install the required libraries:

```bash
pip install flask pandas joblib scikit-learn
```

---

## ▶️ Run the Application

Navigate to the Day-11 folder:

```bash
cd Day-11
```

Run the Flask application:

```bash
python app.py
```

The terminal will provide a local address. Open it in your browser to access the application.

Typically:

```text
http://127.0.0.1:5000/
```

---

## 🖥️ Using the Application

1. Open the Flask web application.
2. Enter the number of **Hours Studied**.
3. Enter **Attendance**.
4. Enter the **Previous Score**.
5. Click the prediction button.
6. The application displays the predicted **Final Score**.

---

## 🔗 Connection with Day-10

Day-10 focused on training and saving the Machine Learning model.

The model was saved as:

```text
student_score_model.pkl
```

Day-11 uses that saved model instead of training the model again.

```text
Day-10
Model Training
     ↓
student_score_model.pkl
     ↓
Day-11
Flask Web Application
     ↓
User Input
     ↓
Prediction
```

This demonstrates how a trained Machine Learning model can be integrated into a real-world web application.

---

## 🧪 Example

### Input

```text
Hours Studied: 8
Attendance: 90
Previous Score: 85
```

### Output

```text
Predicted Final Score: XX.XX
```

The exact prediction depends on the trained model.

---

## 📚 Key Learning Outcomes

By completing this project, I learned:

* How to create a Flask application
* How Flask handles GET and POST requests
* How to create HTML forms for ML applications
* How to receive form data using `request.form`
* How to convert user input into numerical values
* How to create a Pandas DataFrame for prediction
* How to load a saved ML model using Joblib
* How to generate predictions using a trained model
* How to display predictions using Flask templates
* How to connect different stages of an ML project
* How to build a basic ML-powered web application

---

## ⚠️ Important Notes

The feature names used during prediction must match the feature names used when the model was trained:

```text
Hours_Studied
Attendance
Previous_Score
```

The trained model file must also exist at:

```text
Day-10/student_score_model.pkl
```

The Flask application expects the frontend file at:

```text
Day-11/templates/index.html
```

---

## 🎓 Internship Progress

**Day-11 Task:** Deploy the trained Machine Learning model using Flask and create a simple web interface for generating student score predictions.

**Expected Outcome:** A working Flask web application that accepts student information and displays the predicted final score.

---

## 👨‍💻 Author

**Anand**

B.E. Computer Engineering
Government Engineering College Daman
Gujarat Technological University (GTU)
