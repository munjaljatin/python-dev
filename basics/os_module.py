import os

print(os.getcwd())
# print(os.system())

directoryPath = "/Users/Jatin/Developer"
contents = os.listdir(directoryPath)
for item in contents:
  print(item)

print("True and False is",True and False)
print("False and True is",False and True)
print("False and False is",False and False)
print("True and True is",True and True)