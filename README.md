# AI Interview Agent

## Overview
An AI-powered interview simulator that generates technical interview questions, evaluates candidate answers using Google's Gemini API, and produces a structured interview report.

## Features
- Role-based interview questions
- AI-powered answer evaluation
- Per-question scoring
- Overall interview score
- Hiring recommendation
- JSON report generation
- Downloadable interview report
- Graceful API quota error handling

## Tech Stack
- Python
- Streamlit
- Google Gemini API
- python-dotenv

## Installation

pip install -r requirements.txt

## Configure

Create a .env file:

GEMINI_API_KEY=YOUR_API_KEY

## Run

streamlit run app.py

## Folder Structure

...

## Limitations

This project uses the Google Gemini API.
If the API quota is exceeded, the application displays an informative error message and no longer crashes.

## Future Improvements

- Voice interview
- Resume upload
- PDF reports
- User authentication