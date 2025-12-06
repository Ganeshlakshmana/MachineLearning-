# app.py
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import traceback

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

@app.route('/', methods=['GET'])
def index():
    # Render your main form (ensure templates/index.html exists)
    return render_template('index.html', results="")

@app.route('/predictdata', methods=['POST', 'GET'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('index.html', results="")

    try:
        # NOTE: fixed: reading_score -> from reading input, writing_score -> from writing input
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score') or 0),
            writing_score=float(request.form.get('writing_score') or 0)
        )

        pred_df = data.get_data_as_data_frame()
        print("Input DataFrame for prediction:")
        print(pred_df)

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        # Convert result to scalar / nicely formatted string for template
        if hasattr(results, "__len__"):
            pred_value = results[0]
        else:
            pred_value = results

        return render_template('index.html', results=round(float(pred_value), 3))

    except Exception as e:
        # Print full traceback to terminal so you can see what failed
        traceback.print_exc()
        # show user-friendly message
        return render_template('index.html', results=f"Error: {str(e)}")

if __name__ == "__main__":
    # debug=True will show errors in browser and auto-reload on change
    app.run(host="0.0.0.0")
