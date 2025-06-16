
person = {"name": "Ann", "age": 25, "city": "New York"}
print(" \nDictionary:", person)


person["country"] = "USA"
print("\nAfter adding country:", person)


person["age"] = 26
print("\nAfter changing age:", person)


del person["city"]
print("\nAfter removing city:", person)


print("\nName is:", person["name"])


print("\nKeys:", person.keys())


print("\nValues:", person.values())


print("\nItems:", person.items())
