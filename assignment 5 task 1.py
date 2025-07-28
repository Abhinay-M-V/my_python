students = {
    "Alice": 92,
    "Bob": 85,
    "Charlie": 78,
    "Diana": 88
}
name = input("Enter the student's name: ")
if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print(f"Student '{name}' not found.")
