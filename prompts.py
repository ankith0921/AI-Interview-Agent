QUESTION_PROMPT = """
You are an experienced technical interviewer.

The candidate is applying for the following role.

Role: {role}

Experience: {experience}

Generate exactly FIVE interview questions.

Rules:
- Questions should be relevant to the role.
- Mix easy and medium difficulty.
- Do NOT include answers.
- Number each question.
"""

EVALUATION_PROMPT = """
You are a senior technical interviewer.

Evaluate the candidate's answer.

Question:
{question}

Candidate Answer:
{answer}

Give your response EXACTLY in this format:

Score: X/10

Strengths:
- ...

Weaknesses:
- ...

Ideal Answer:
...
"""
FINAL_REPORT_PROMPT = """
You are a Senior Technical Hiring Manager.

Based on the following interview evaluation:

{results}

Generate:

Overall Score Summary

Strengths (bullet points)

Weaknesses (bullet points)

Topics to Improve

Hiring Recommendation:
Choose one:
- Hire
- Consider
- Needs Improvement

Give a brief explanation.
"""