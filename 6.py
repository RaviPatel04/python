# Strings Slicing and Operations on Strings

fruit = 'mango'
print(len(fruit))
print(fruit[:])
print(fruit[1:4])
print(fruit[2:5])
print(fruit[-3:-1])
print(fruit[::])
print(fruit[::-1])


# String Methods
str = "!!Good morning!!!Good night!!!!"
print(str.count("o"))
print(str.endswith("!"))
print(str.startswith("!"))
print(str.center(20))
print(str.replace("morning", "evening"))
print(str.upper())
print(str.lower())

str1 = "jsdb21"
print(str1.isalnum())
print(str1.isalpha())
print(str1.isspace())

str2 = "hello, ravi ,How are you?"
print(str2.split(','))

s3=" ".join([str1,str2])
print(s3)