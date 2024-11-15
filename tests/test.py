import pandas as pd

fetch_jobs= [
    {
        "currency": "NGN",
        "exp_requirement": "3",
        "id": 2,
        "jobDescription": "Developing software solutions, participating in code reviews, and building scalable applications.",
        "location": "Lagos, Nigeria",
        "qualifications": "Bachelor's degree in Computer Science or related field, 3+ years experience in software development.",
        "salary": 800000,
        "title": "Software Engineer"
    },
    {
        "currency": "NGN",
        "exp_requirement": "2+",
        "id": 3,
        "jobDescription": "Analyze complex data sets, develop machine learning models, and present data-driven insights.",
        "location": "Abuja, Nigeria",
        "qualifications": "Master's degree in Data Science or related field, proficiency in Python, R, SQL, and machine learning.",
        "salary": 950000,
        "title": "Data Scientist"
    },
    {
        "currency": "NGN",
        "exp_requirement": "4",
        "id": 4,
        "jobDescription": "Oversee product development, collaborate with cross-functional teams, and ensure product timelines are met.",
        "location": "Port Harcourt, Nigeria",
        "qualifications": "Bachelor's degree in Business or related field, 5+ years of experience in product management.",
        "salary": 1200000,
        "title": "Product Manager"
    },
    {
        "currency": "NGN",
        "exp_requirement": "2+",
        "id": 5,
        "jobDescription": "Design user-centric interfaces, conduct user research, and work closely with developers to implement designs.",
        "location": "Ibadan, Nigeria",
        "qualifications": "Bachelor's degree in Design or related field, proficiency in Adobe XD, Figma, or Sketch.",
        "salary": 600000,
        "title": "UX/UI Designer"
    },
    {
        "currency": "NGN",
        "exp_requirement": "10+",
        "id": 6,
        "jobDescription": "Develop and execute online marketing strategies, manage social media campaigns, and analyze marketing performance.",
        "location": "Kaduna, Nigeria",
        "qualifications": "Bachelor's degree in Marketing, 3+ years experience in digital marketing, knowledge of SEO and SEM.",
        "salary": 750000,
        "title": "Digital Marketing Manager"
    },
    {
        "currency": "NGN",
        "exp_requirement": "3+",
        "id": 7,
        "jobDescription": "Create visual content for digital and print media, develop branding materials, and collaborate with marketing teams.",
        "location": "Lagos, Nigeria",
        "qualifications": "Bachelor's degree in Graphic Design or related field, proficiency in Adobe Creative Suite (Photoshop, Illustrator).",
        "salary": 550000,
        "title": "Graphic Designer"
    },
    {
        "currency": "NGN",
        "exp_requirement": "7+",
        "id": 8,
        "jobDescription": "Assist customers in-store, maintain product displays, and handle sales transactions.",
        "location": "Abuja, Nigeria",
        "qualifications": "High school diploma, strong communication skills, experience in retail sales.",
        "salary": 300000,
        "title": "Sales Girl"
    },
    {
        "currency": "NGN",
        "exp_requirement": "3+",
        "id": 9,
        "jobDescription": "Provide customer service through phone, email, and chat, resolve issues and process requests.",
        "location": "Enugu, Nigeria",
        "qualifications": "Bachelor's degree in Communications or related field, 1+ years experience in customer support.",
        "salary": 400000,
        "title": "Customer Support Representative"
    },
    {
        "currency": "NGN",
        "exp_requirement": "5+",
        "id": 10,
        "jobDescription": "Manage project timelines, coordinate with stakeholders, and ensure deliverables are met on time and within budget.",
        "location": "Benin City, Nigeria",
        "qualifications": "Bachelor's degree in Project Management, PMP certification, 4+ years of project management experience.",
        "salary": 1000000,
        "title": "Project Manager"
    },
    {
        "currency": "NGN",
        "exp_requirement": "7+",
        "id": 11,
        "jobDescription": "Oversee recruitment, employee relations, and organizational development.",
        "location": "Lagos, Nigeria",
        "qualifications": "Bachelor's degree in Human Resources or related field, 5+ years of experience in HR management.",
        "salary": 950000,
        "title": "Human Resources Manager"
    }
]
def get_job_by_id(job_id):
    df = pd.DataFrame(fetch_jobs)
    filtered_job = df[df["id"] == job_id]
    # Return the first matching job as a dictionary
    print(filtered_job.iloc[0].to_dict() if not filtered_job.empty else None)

get_job_by_id(2)