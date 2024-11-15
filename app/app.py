from flask import Blueprint, flash, redirect, render_template, jsonify, request, url_for
import pandas as pd
import os
from app import create_app
from app.database import fetch_jobs

jobs = fetch_jobs()
bp = Blueprint('app', __name__)

@bp.route('/')
def home():
    return render_template('index.html', jobs=jobs)  

@bp.route('/api/jobs')
def list_jobs():
    return jsonify(jobs)

def get_job_by_id(job_id):
    df = pd.DataFrame(jobs)
    filtered_job = df[df["id"] == job_id]
    # Return the first matching job as a dictionary
    return filtered_job.iloc[0].to_dict() if not filtered_job.empty else None


@bp.route('/apply/<int:job_id>', methods=['GET', 'POST'])
def job_details(job_id):
    job = get_job_by_id(job_id)  # Fetch job data
    if request.method == 'POST':
        # Process the application form
        name = request.form['name']
        email = request.form['email']
        resume = request.files['resume']
        
        flash("Your application has been submitted successfully!", "success")
        return redirect(url_for('app.job_details', job_id=job_id))
    
    return render_template('job_details.html', job=job)

if __name__ == "__main__":
    app = create_app()  # Create the app instance
    app.run(debug=True)
