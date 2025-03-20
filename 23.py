file_path = "new_file.txt"  
word_to_find = "line"      
word_to_replace = "lineline"   


with open(file_path, "r") as file:
    content = file.read()


content = content.replace(word_to_find, word_to_replace)


with open(file_path, "w") as file:
    file.write(content)

print(f"Replaced all occurrences of '{word_to_find}' with '{word_to_replace}'.")
