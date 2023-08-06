# Dictionaries

# dict = {
#     "name" : "Ravi",
#     "surname" : "Patel",
#     "age" : "18",
#     "study" : "computer engineering"
# }
# print(dict)
# print(dict.keys())
# print(dict.values())
# print(dict["name"])
# print(dict["study"])

# Dictionary Methods

marks1 = {
    3 : 25,
    13 : 20,
    23 : 40,
    33 : 35,
    43 : 12
}
marks2 = {
    53 : 30,
    63 : 16,
    73 : 15
}
marks1.update(marks2)
print(marks1)

marks1.pop(43)
print(marks1)

marks1.clear()
print(marks1)