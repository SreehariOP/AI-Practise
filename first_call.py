from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq()  # reads GROQ_API_KEY from the environment

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": "You are a witty travel guide"},
        {"role": "user", "content": "Suggest one thing to do in Bangalore"},
    ]
)

print(response.choices[0].message.content)
