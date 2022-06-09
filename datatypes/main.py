# String
name = "Christian Abrokwa"
print(type(name))
print(name[0:9:2]) # Starts at 0, end at 3 and step(differnce) is 2
print(name[5:])
print(name[:])
print(name[-1])
print(name[6])
print(f"The lowercase version of {name} is {name.upper()}")
print(f"The number of characters in {name} is {len(name)}")
print(name*3)
age = "14"
print(age*3)
print()
print()

# Integer
age = 12.4
print(type(age))
print(age *3)
print(age)
print()
print()

# List(arrays)
names = ["Daquiver", "Chrsitian", "Yaw", "Asher", "Aziz"]
print(type(names))
print(names[0])
print(names[-1])
print("yaw" in names)
names.append("Kwame")
print(names)
print(f"The number of elements in list names is {len(names)}")
print()
print()

# Dictionaries
food_count = {'apple': 0, "pawpaw": 3, "banku": 4, 'yam': 12}
phone_model = {'huawei': 'y7', 'iphone': 'iphoneMax', 'Nokia': 'Nokia3310', 'samsung': 'A52'}
print(type(food_count))
food_count['pawpaw'] = 27
print(food_count)

