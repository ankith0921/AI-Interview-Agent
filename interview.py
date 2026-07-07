import google.generativeai as genai
from prompts import QUESTION_PROMPT

def generate_questions(model, role, experience):

    prompt = QUESTION_PROMPT.format(
        role=role,
        experience=experience
    )

    response = model.generate_content(prompt)

    questions = []

    for line in response.text.split("\n"):
        if line.strip() and line[0].isdigit():
            questions.append(line.split(".", 1)[1].strip())

    return questions