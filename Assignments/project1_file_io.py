# Project 1: File I/O - Jesus Gudino

# Create and write to a text file
with open("example.txt", "w") as file:
    file.write("Hello, this is my file I/O project.\n")
    file.write("I created this file using Python!\n")

# Read the file
with open("example.txt", "r") as file:
    content = file.read()

print("File content:")
print(content)
