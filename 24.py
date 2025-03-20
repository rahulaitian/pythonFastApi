import pickle

data = {"name": "Rahul", "age": 25, "city": "Bijnor"}

file_path = "data.pkl"

with open(file_path, "wb") as file:
    pickle.dump(data, file)
print("Object serialized and saved successfully.")

with open(file_path, "rb") as file:
    loaded_data = pickle.load(file)

print("Deserialized object:", loaded_data)
