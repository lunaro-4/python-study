# Dictionaries
my_dict : dict = {
        "First_value" : 123,
        "Second_value" : True
        }
print("Value exists: ", my_dict.get("First_value"))
print("Value dows not exist: ", my_dict.get("Third_value"))
my_dict["Third_value"] = "Super String"
print("Value to be removed: ", my_dict.pop("Second_value"))
print("Final dictionary: ", my_dict)
print('\n')


# Sets
my_set : set = {1, "Super String", 21.12, 1, "Super String"}
print("My set: ", my_set)
my_set.add(12.21)
my_set.add((1, 2))
my_set.remove(21.12)
print("Modified set: ", my_set)


