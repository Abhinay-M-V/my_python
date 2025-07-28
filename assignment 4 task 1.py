try:
    with open("sam.txt", "r") as file:
        print("Reading file contents:")
        for line in file:
            print(line, end="")
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
