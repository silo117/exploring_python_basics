a = 1
b = 2

print(a == b) #equivalence operator, returns False -- note that single = is assigning a value, == is comparing values
       #additionally note that the boolean value is False, not false 
print(a != b) #inequity operator, returns True
print(a > b)  #greater than, returns False
print(a <= b) #less than or equal to, returns True

c = "a"
d = "A"
e = "z"
f = "1"
g = "01"
h = "10"
i = "0100"

print(c == d) #strings are case sensitive, returns False
print(c > e) #a comes first so z has a higher value, returns False
print(c > d) #comparison is based off of letter order with capital letters coming before lower case, so lower case has a higher value than capital, returns True
print(c > f) #string formatted digits come before lower case, returns True
print(d > f) #string formatted digits come before capitals, returns True
print(f == g) #even though numerically equal, the leading zero does change the string so this returns False
print(f > g) #comparison appears to look at first character, returns true
print(f > h) # at this point I tire of checking individual relationships to tease out the rules, so onto sort()
print(f == h)
print(f > i)

fullList = "abcdefghjklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()_+-=? " #I broke this a bit earlier with curly braces, I think it's because
            #I unintentionally espcaped the leading one out.  I may circle back to that to make this list more complete
charlist = [ x for x in fullList] #this splits out each character in the refernced variable and adds it to a list
charlist.sort() #sort method puts all members of a list in ascending order
print(charlist) #will print ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '=', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '~']

'''so now I'm curious about how 2nd character and beyond are compared because of how g, h, and i were treated above'''

j = "aa"
k = "ab"
l = "a a"
m = " aa"
n = "aa "
o = "aaa"

print( j > k) #returns False
print( j > l) #returns True
print( j > m) #returns True
print( j > n) #returns False
print( j > o) #returns False