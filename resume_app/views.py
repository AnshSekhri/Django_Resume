from django.shortcuts import render

def resume_view(request):
    context = {
        'name': "Ansh Sekhri",
        'contact': {
            'location': "Una, India",
            'email': "sekhriansh556@gmail.com",
            'phone': "+91 7018954936",
            'linkedin': "https://linkedin.com/in/yourprofile",
            'github': "https://github.com/yourprofile",
        },
        'skills': ["Python", "Django", "REST APIs", "SQL", "HTML/CSS", "Git", "Tableau"],
        'experience': [
            {
                'role': "Python/Django Intern",
                'company': "Suvidha Mahila Mandal",
                'duration': "Aug 2023 - Sep 2023",
                'description': [
                    "Developed a text summarization pipeline in Python.",
                    "Collaborated with researchers to optimize summarization methods.",
                ],
            },
            {
                'role': "Data Research Analyst Intern",
                'company': "Learn With Leaders",
                'duration': "Dec 2022 - Jan 2023",
                'description': [
                    "Conducted data research for educational programs.",
                    "Analyzed data using SQL and Excel.",
                ],
            },
        ],
        'education': [
            {"degree": "B.Tech in AI & ML", "school": "CGC College of Engineering", "year": "2022 - 2026"},
            {"degree": "Senior Secondary (XII)", "school": "M.I.A D.A.V Public School", "year": "2022"},
        ],
        'projects': [
            {"title": "Music Recommendation System", "description": "Built a content-based filtering system using Django and Python."},
            {"title": "E-Commerce Web App", "description": "Developed a platform with product management and payment gateway integration."},
            {"title": "Blogging Platform", "description": "Implemented CRUD functionalities for blogs with user authentication."},
        ],
        'achievements': [
            "Selected for Smart India Hackathon 2024.",
            "HackerRank Python 3-star badge.",
        ],
        'soft_skills': ["Problem-Solving", "Team Collaboration", "Communication", "Time Management"],
    }
    return render(request, 'resume_app/resume.html', context)
