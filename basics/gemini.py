from google import genai

client = genai.Client(api_key="AIzaSyDil2NuAxj4jCsu_Mun-0TPl3R-BCsJpJY")

prompt = input()

response = client.models.generate_content(
  model = "gemini-2.5-flash",
  contents = prompt
)

# print(response.text)

with open("content.md", "w") as file:
  file.write(response.text)