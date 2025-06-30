name = input("Enter your name: ")
print("Good Afternoon", name)
print(f"Good Afternoon {name}")


letter = """ Dear <|Name|>
          You're Selected!
          <|Date|>
"""

print(letter.replace("<|Name|>", name).replace("<|Date|>", "30-06-2025"))

text = "Too  Many  Spaces  "
print("Number of Double spaces found are", text.count("  "))

newText = text.replace("  ", " ")
print(newText)
