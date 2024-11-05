from flask import Blueprint, render_template, jsonify

from app import create_app

# Define a Blueprint for your app
bp = Blueprint('app', __name__)

JOBS = [
    {
        "id": 1,
        "title": "Software Developer",
        "location": "Lagos, Nigeria",
        "exp_requirement": "2+ years",
        "salary": "$50,000 per annum"
    },
    {
        "id": 2,
        "title": "Fashion Designer",
        "location": "Lagos, Nigeria",
        "exp_requirement": "5+ years",
        "salary": "$400 per month"
    },
    {
        "id": 3,
        "title": "Graphics Designer",
        "location": "Lagos, Nigeria",
        "exp_requirement": "2+ years",
        "salary": "$800 per month"
    },
    {
        "id": 4,
        "title": "Data Scientist",
        "location": "Abuja, Nigeria",
        "exp_requirement": "1+ years"
    },
]

@bp.route('/')
def home():
    return render_template('index.html', jobs=JOBS)  # Render the HTML file with jobs

@bp.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)  # Return the jobs in JSON format

if __name__ == "__main__":
    app = create_app()  # Create the app instance
    app.run(debug=True)
