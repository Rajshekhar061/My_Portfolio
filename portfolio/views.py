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
            "React",
            "NLP",
            "RAG",
            "PostgreSQL",
        ],
        "projects": [
            {
                "title": "RAG AI Assistant",
                "description": "A FastAPI-powered assistant using semantic search and LLMs to answer domain-specific queries.",
                "stack": "FastAPI · LLM · Semantic Search · Python",
                "github": "https://github.com/Rajshekhar061/RAG-based-Assistant",
                "demo": "Working on deploying scalable AI applications with real-time demos.",
            },
            {
                "title": "AI Code Reviewer",
                "description": "LLM-based code analysis tool that checks quality, style, and edge cases in real time.",
                "stack": "LLM · Python · Code Analysis · API",
                "github": "https://github.com/Rajshekhar061/AI-Code-Reviewer",
                "demo": "Working on deploying scalable AI applications with real-time demos.",
            },
            {
                "title": "Resume Screener",
                "description": "NLP-driven screening system that filters resumes and highlights top candidate fit scores.",
                "stack": "NLP · Python · PostgreSQL · Automation",
                "github": "https://github.com/Rajshekhar061/AI-Resume-Screener",
                "demo": "Working on deploying scalable AI applications with real-time demos.",
            },
        ],
        "experience": {
            "role": "Python Fullstack Internship (Training Program)",
            "company": "OCAC Odisha",
            "date": "April 2026 – Present",
            "description": "Building Django web apps, REST APIs, React interfaces, and PostgreSQL-backed services with a focus on clean code and scalable design.",
        },
        "contact": {
            "email": "mailto:rajshekhar061@gmail.com",
            "github": "https://github.com/Rajshekhar061",
            "linkedin": "https://www.linkedin.com/in/rajshekhar-singh-572574276",
        },
    }
    return render(request, "portfolio/home.html", context)
