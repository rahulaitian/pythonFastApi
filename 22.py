file_path = "new_file.txt"

with open(file_path, "r") as file:
    text = file.read()
    word_count = len(text.split())  

print(f"Total number of words: {word_count}")
