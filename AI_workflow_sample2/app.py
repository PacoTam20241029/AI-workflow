from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from models.random_forest import train_and_evaluate

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Collect form data
        data = {
            'Pregnancies': request.form['Pregnancies'],
            'Glucose': request.form['Glucose'],
            'BloodPressure': request.form['BloodPressure'],
            'SkinThickness': request.form['SkinThickness'],
            'Insulin': request.form['Insulin'],
            'BMI': request.form['BMI'],
            'DiabetesPedigreeFunction': request.form['DiabetesPedigreeFunction'],
            'Age': request.form['Age'],
            'Outcome': request.form['Outcome']
        }
        df = pd.DataFrame([data])
        df.to_csv('data/diabetes.csv', mode='a', header=False, index=False)
        accuracy = train_and_evaluate()
        return f'Workflow created! Model accuracy: {accuracy}'
    return redirect(url_for('index'))

if __name__ == '__main__':
        app.run(debug=True)