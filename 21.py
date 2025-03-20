file_path = "new_file.txt"
with open(file_path, "w") as file:
    file.write("Hello, this is line 1.\n")
    file.write("This is line 2.\n")
    file.write("And this is line 3.\n")

with open(file_path, "r") as file:
    for line in file:
        print(line.strip()) 
