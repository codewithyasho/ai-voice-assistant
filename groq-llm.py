from groq import Groq
from dotenv import load_dotenv
load_dotenv()

client = Groq()
completion = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
          "role": "user",
            "content": "what is the capital of france?"
        }
    ],
    temperature=0.2,
)

result = completion.choices[0].message.content
print(result)
