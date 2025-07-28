user_input = input("Enter some data: ")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")

additional_data = input("Enter additional data to append: ")
with open("output.txt", "a") as file:
    file.write(additional_data + "\n")

with open("output.txt", "r") as file:
    content = file.read()

print("\nFinal content of 'output.txt':")
print(content)
