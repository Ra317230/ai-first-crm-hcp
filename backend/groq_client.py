from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_groq(prompt):
    response = client.chat.completions.create(
        model="gemma2-9b-it",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content