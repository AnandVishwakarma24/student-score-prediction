# ---- Variables & Data Types ----
name = "Anand Vishwakarma"
study_hours = 5
score = 75.5
is_passed = True
print("Name:", name) 
print("Study Hours:", study_hours)
print("Score:", score)
print("Passed:", is_passed)
# ---- Operators ----
a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)
# ---- Conditionals ----
def grade_category(score):
    if score >= 90:
        return "Grade A"
    elif score >= 60:
        return "Grade B"
    else:
        return "Grade C"
print("Grade:", grade_category(score))
# ---- Loops ----
print("Multiplication Table of 5:")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")
total = 0
n = 1
while n <= 10:
    # ---- Variables & Data Types ----
    name = "Anand Vishwakarma"
    study_hours = 5
    score = 75.5
    is_passed = True
    print("Name:", name)
    print("Study Hours:", study_hours)
    print("Score:", score)
    print("Passed:", is_passed)
    # ---- Operators ----
    a = 10
    b = 3
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)
    print("Floor Division:", a // b)
    print("Modulus:", a % b)
    print("Exponent:", a ** b)
    # ---- Conditionals ----
    def grade_category(score):
        if score >= 90:
            return "Grade A"
        elif score >= 60:
            return "Grade B"
        else:
            return "Grade C"
    print("Grade:", grade_category(score))
    # ---- Loops ----
    print("Multiplication Table of 5:")
    for i in range(1, 11):
        print(f"5 x {i} = {5 * i}")
    total = 0
    n = 1
    while n <= 10:
        total += n
        n += 1
    print("Sum of first 10 numbers:", total)
    # ---- Functions ----
    def predict_score(hours):
        # Simple placeholder formula, real model comes later
        return hours * 10
    for h in [1, 3, 5, 7, 9]:
        predicted = predict_score(h)
        print(f"Study Hours: {h} -> Predicted Score: {predicted} -> {grade_category(predicted)}")