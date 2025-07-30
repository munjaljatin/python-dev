import os
from google import genai

api = os.environ.get("GEMINI_API_KEY")
print(api)

client = genai.Client()

prompt = input()

response = client.models.generate_content(
  model = "gemini-2.5-flash",
  contents = prompt
)

# print(response.text)

with open("content.md", "w") as file:
  file.write(response.text)