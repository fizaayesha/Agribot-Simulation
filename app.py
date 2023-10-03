import pandas as pd
from flask import Flask, render_template  # Import render_template

app = Flask(__name__)

@app.route('/')
def display_data():
    dataset = pd.read_csv('Crop_recommendation.csv')
    y_test = dataset['label'].values
    y_pred = ...  # Your predicted values
    data = [{'Real Values': real, 'Predicted Values': pred} for real, pred in zip(y_test, y_pred)]
    return render_template('template.html', data=data)

if __name__ == '__main__':
    app.run()