# AI Interview Agent

An AI-powered interview simulator built with **Streamlit** and **Google Gemini AI**. The application generates role-specific interview questions, evaluates candidate responses, provides detailed feedback with scores, and generates a downloadable interview report.

---

## Features

- Generate role-based technical interview questions
- AI-powered evaluation of candidate answers
- Detailed feedback for every response
- Per-question scoring
- Overall interview score
- Hiring recommendation
- Downloadable JSON interview report
- Graceful handling of Gemini API quota errors
- Simple and interactive Streamlit interface

---

## Tech Stack

- Python
- Streamlit
- Google Gemini API
- python-dotenv

---

## Project Structure

```
AI-Interview-Agent/
│── app.py
│── interview.py
│── evaluator.py
│── prompts.py
│── requirements.txt
│── README.md
│── .gitignore
│── Screenshots/
```

---

## Installation

### 1. Download or clone the repository.

### 2. Open a terminal in the project folder.

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

---

## Gemini API Setup

This project requires a **Google Gemini API Key**.

### Step 1

Generate an API key from:

https://aistudio.google.com/app/apikey

### Step 2

Create a file named **`.env`** in the **root folder** of the project (the same folder that contains `app.py`).

Your project should look like this:

```
AI-Interview-Agent/
│── app.py
│── interview.py
│── evaluator.py
│── prompts.py
│── .env
```

### Step 3

Add the following line to the `.env` file:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Replace `YOUR_GEMINI_API_KEY` with the API key you generated from Google AI Studio.

---

## Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open automatically in your browser at:

```
http://localhost:8501
```

---

## Screenshots

The repository contains screenshots demonstrating:

- Home Page
- Role Selection
- Interview Questions
- AI Evaluation
- Final Results

---

## Output

After the interview, the application provides:

- AI-generated evaluation for each answer
- Individual question scores
- Overall interview score
- Hiring recommendation
- Downloadable interview report in JSON format

---

## Limitations

- Uses the Google Gemini API for question generation and evaluation.
- An active internet connection is required.
- If the Gemini API quota is exceeded, the application displays a user-friendly error message instead of crashing.
- Currently supports text-based interviews only.

---

## Future Improvements

- Voice interview
- Resume upload
- PDF reports
- User authentication

# About the Author

## Ankith Kanthyappa Nataraj

Computer Science Engineering Graduate with interests in:

- Artificial Intelligence
- Machine Learning
- Natural Language Processing
- Data Science
- Software Engineering

**GitHub**

https://github.com/ankith0921

**LinkedIn**

https://www.linkedin.com/in/ankith-kn-9b7a6329b

---

# License

This project is licensed under the **MIT License**.

See the `LICENSE` file for details.
