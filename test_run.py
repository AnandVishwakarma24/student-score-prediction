import sys
from pathlib import Path

print('Running test_run.py')
print('Python:', sys.version.replace('\n',' '))

base = Path(__file__).parent
DATA_PATH = base / 'student' / 'data' / 'student_scores.csv'
MODEL_DIR = base / 'student' / 'models'
MODEL_PATH = MODEL_DIR / 'linear_regression.joblib'

# Prevent local modules in the repo root from shadowing installed packages
base_str = str(base)
if sys.path and sys.path[0] in (base_str, ''):
    sys.path.pop(0)

try:
    import pandas as pd
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
    import joblib
except Exception as e:
    print('Missing package or import error:', e)
    print('Please install required packages: pandas scikit-learn joblib')
    raise

if not DATA_PATH.exists():
    raise FileNotFoundError(f'Data file not found: {DATA_PATH}')

print('Loading data from', DATA_PATH)
df = pd.read_csv(DATA_PATH)
print('Data shape:', df.shape)
print(df.head().to_string(index=False))

# Basic checks
if 'Hours' not in df.columns or 'Scores' not in df.columns:
    raise ValueError('Expected columns Hours and Scores in CSV')

X = df[['Hours']]
y = df['Scores']

# Train model
model = LinearRegression()
model.fit(X, y)
print('Trained LinearRegression. Coef:', model.coef_, 'Intercept:', model.intercept_)

MODEL_DIR.mkdir(parents=True, exist_ok=True)
joblib.dump(model, MODEL_PATH)
print('Saved model to', MODEL_PATH)

# Predict sample
sample = [[9.25]]
pred = model.predict(sample)
print(f'Prediction for {sample[0][0]} hours: {pred[0]:.2f}')

# Evaluation on training data
y_pred = model.predict(X)
print('MAE:', mean_absolute_error(y, y_pred))
print('MSE:', mean_squared_error(y, y_pred))
print('R2:', r2_score(y, y_pred))

# Import and use day-11 script
import importlib.util
mod_path = base / 'student' / 'day-11_prediction_app.py'
spec = importlib.util.spec_from_file_location('day11', str(mod_path))
day11 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(day11)
predict_for = getattr(day11, 'predict_for')

print('day-11 prediction function output for 9.25:', predict_for(9.25))

print('All checks completed successfully')
