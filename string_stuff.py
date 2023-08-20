a = "Potato"
b = "P"
c = "o"
d = "Egg"

print("Upper", a.upper()) #returns POTATO
print("Lower", a.lower()) #returns potato
print("Numeric check", a.isalpha()) #returns true -- will return True if it only contains characters and is NOT empty
print("Alphaumeric check", a.isalnum()) #returns true -- will return True if only contains numbers or characters and is NOT empty
print("Decimal check", a.isdecimal())# returns false -- will return True if only contains numbers (check if float/int matters) and is NOT empty
print("Lowercase check", a.islower())#returns false -- will return True if string is lower case (check on what happens with numbers)
print("Uppercase check", a.isupper())#returns false -- will return True if string is Upper case (same as above, also check empty strings)
print("Starting letter check --looking for",b,"--", a.startswith(b))#returns true -- will return True if you match the beginning character
print("Ending letter check --looking for",c,"--", a.endswith(c))#returns false -- same as above -- need to check empty, space, and case
print("String replacement --replacing", a, "with", d, a.replace("Potato", d))#replaces all instances of specified substring, neeed to check on if it works with letters.  also args are (search_string, replacement_string, number to replace)



print(a.join())



print(a.strip())


find()


len()
'''make note that each of these doesn't change the string as strings are immutable. they just return a copy of the string.'''