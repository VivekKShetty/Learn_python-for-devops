str1 = "Hello"
str2 = "World"

Concat = str1 + " " + str2
print(Concat)
print(len(Concat))
Uppercase = Concat.upper()
print(Uppercase)
print(Concat.lower())
New_String = Concat.replace("World", "Earth")
print("Modiflied text:", New_String)
print(Concat.split())
Strip_string ="     Hello to Python             "
print("Proper String:", Strip_string.strip())
substring = "to"
if substring in Strip_string:
    print(substring, "found in text")





