#!/usr/bin/env bash
export FLASK_APP=./src/main.py
source $(pipenv --venv)/bin/activate
flask run -h 0.0.0.0

curl -X POST -H 'Content-Type: application/json' -d '{
  "title": "TypeScript Advanced Exam",
  "description": "Tricky questions about TypeScript."
}' http://0.0.0.0:5000/exams

curl http://0.0.0.0:5000/exams