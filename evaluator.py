import google.generativeai as genai
from prompts import EVALUATION_PROMPT

def evaluate_answer(model, question, answer):

    prompt = EVALUATION_PROMPT.format(
        question=question,
        answer=answer
    )

    response = model.generate_content(prompt)

    return response.text