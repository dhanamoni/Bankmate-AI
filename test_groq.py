
import os
from dotenv import load_dotenv
from groq import Groq

# Load the API key from the .env file
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("ERROR: GROQ_API_KEY not found in .env")
else:
    try:
        client = Groq(api_key=api_key)

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "user",
                    "content": "Reply with exactly: Groq connection successful"
                }
            ],
            temperature=0
        )

        print("Groq response:")
        print(response.choices[0].message.content)

    except Exception as error:
        print("Groq connection failed.")
        print("Error type:", type(error).__name__)
        print("Check your API key, internet connection, and API limits.")