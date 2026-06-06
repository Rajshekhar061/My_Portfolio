from django.shortcuts import render


def home(request):
    context = {
        "hero": {
            "name": "Rajshekhar Singh",
            "title": "AI Engineer & Full Stack Developer",
            "intro": "I build AI-powered web applications using Django, FastAPI, and modern machine learning APIs.",
        },
        "skills": [
            "Python",
            "Django",
            "FastAPI",
            "Django REST Framework",
            "JavaScript",
            "HTML",
            "CSS",
            "LLM Integration",
            "Prompt Engineering",
            "NLP",
            "RAG (Retrieval-Augmented Generation)",
            "PostgreSQL",
            "SQLite",
            "REST APIs",
            "Authentication & Authorization",
            "WebSockets (Basic)",
            "Git & GitHub",
            "System Design (Basic Backend)"
        ],
        "projects": [
            {
                "title": "MockMate AI",
                "description": "Django-based AI mock interview platform that simulates real interview scenarios and evaluates responses using LLM-driven analysis, providing structured feedback on communication, accuracy, and problem-solving approach.",
                "stack": "Django · Python · LLM Integration · REST APIs · JavaScript · HTML · CSS",
                "github": "https://github.com/Rajshekhar061/MockMate",
                "demo": "https://mockmate-v7if.onrender.com/",
            },
            
            {
                "title": "AI Code Reviewer",
                "description": "LLM-based code analysis tool that checks quality, style, and edge cases in real time.",
                "stack": "LLM · Python · Code Analysis · API",
                "github": "https://github.com/Rajshekhar061/AI-Code-Reviewer",
                "demo": "https://code-reviewer-5afr.onrender.com/",
            },
            {
                "title": "RAG AI Assistant",
                "description": "A FastAPI-powered assistant using semantic search and LLMs to answer domain-specific queries.",
                "stack": "FastAPI · LLM · Semantic Search · Python",
                "github": "https://github.com/Rajshekhar061/RAG-based-Assistant",
                "demo": "Working on deploying scalable AI applications with real-time demos.",
            },
            
        ],
        "experience": {
            "role": "Python Fullstack Internship",
            "company": "OCAC Odisha",
            "date": "August 2025 – April 2026",
            "description": "Building Django web apps, REST APIs, React interfaces, and PostgreSQL-backed services with a focus on clean code and scalable design.",
        },
        "contact": {
            "email": "mailto:rajshekhar061@gmail.com",
            "github": "https://github.com/Rajshekhar061",
            "linkedin": "https://www.linkedin.com/in/rajshekhar-singh-572574276",
        },
    }
    return render(request, "portfolio/home.html", context)
