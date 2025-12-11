from flask import Flask, jsonify, request
import json

app = Flask(__name__)

students = [
    {
        "id": 1,
        "name": "Jordan Johnson",
        "class": "Year 8",
        "subjects": {
            "Maths": 98,
            "Science": 90,
            "English": 88,
            "History": 90,
            "ICT": 96
        },
        "total": 462,
        "average": 92.6,
        "grade": "A*"
    }, 
    {
        "id": 2,
        "name": "Kevin Johnson",
        "class": "Year 8",
        "subjects": {
            "Maths": 94,
            "Science": 96,
            "English": 91,
            "History": 89,
            "ICT": 99
        },
        "total": 469,
        "average": 93.8,
        "grade": "A*"
    },
    {
        "id": 3,
        "name": "Marcus Rashy",
        "class": "Year 8",
        "subjects": {
            "Maths": 85,
            "Science": 82,
            "English": 88,
            "History": 91,
            "ICT": 87
        },
        "total": 433,
        "average": 86.6,
        "grade": "A"
    },
    {
        "id": 4,
        "name": "Sofia Banda",
        "class": "Year 8",
        "subjects": {
            "Maths": 79,
            "Science": 84,
            "English": 92,
            "History": 87,
            "ICT": 90
        },
        "total": 432,
        "average": 86.4,
        "grade": "A"
    },
    {
        "id": 5,
        "name": "Patrick John",
        "class": "Year 8",
        "subjects": {
            "Maths": 88,
            "Science": 76,
            "English": 80,
            "History": 85,
            "ICT": 93
        },
        "total": 422,
        "average": 84.4,
        "grade": "A"
    }
]

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the year 8 students scores API",
        "endpoints": {
            "GET  /api/students": "List all the students"
        }
    })

@app.route("/api/students", methods=["GET"])
def get_students():
    return jsonify({
        "success": True,
        "data": students
    }), 200