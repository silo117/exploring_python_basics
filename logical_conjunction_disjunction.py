p = True
q = False
print("\nFor an initial value of p is", p, "and q is", q, ", the following statements will evaulate to:\n")
print("Conjunction/And")
print("p and q is",p,"and", q, "which evaluates to", p and q)
print("Not p and q is",not p,"and", q, "which evaluates to", not p and q)
print("p and not q is",p,"and", not q, "which evaluates to", p and not q)
print("Not p and not q is",p,"and", q, "which evaluates to", not p and not q,"\n")

print("Disjunction/Or", )
print("p or q is", p, "or", q, "which evaluates to", p or q)
print("not p or q is", not p, "or", q, "which evaluates to", not p or q)
print("p or not q is", p, "or", not q, "which evaluates to", p or not q)
print("not p or not q is",not p,"or", not q, "which evaluates to", not p or not q,"\n"*2)

''''A note, some values in Python carry an implied boolean value (true or false) without being explicitly True or False.  IF any of these values are used in a logical statement
it will act as though it has the associated boolean value.  Additionally, the intersection of some functions with bools will behave in somewhat unexpected ways if  you don't account
for this behavior'''

print("This is the boolean value of 0:",bool(0))
print("This is the boolean value of 1:",bool(1), "\n"*2)
 
print ("Conjunctions")
'''Another way to read an "and" statement in Python is "only bother with the second value if the first is true", so if the first value is not true, it will return the first value.  
Otherwise it'll return the 2nd value'''
print(0 and 1) #returns 0
print(False and "hi") #returns 0
print("boo" and "hi") #returns "hi"
print([] and False) #returns []
print(False and [],"\n") #returns False

print("Disjunctions")
print(0 or 1) #this will return 1 because it ignores the "false" 0 and sees the 1 as the first "true"
print(False or "hi") #returns "hi", again ignoring the initial false value
print("boo" or "hi") #returns "boo", as the first value is a non-false value
print([] or False) #here we discover that an empty set is viewed as more false than False -- probably something metaphysical going on here
print(False or [],"\n"*2) #nah, just joking above when there is no value that can be understood as nonfalse, it simply returns the 2nd value

"""There doesn't seem to be an xor in Python outside of the bitwise operator ^ which won't work for a lot of things so I guess what follows is a way to implement via function"""

def xor(xorP=True, xorQ=False): #initializing with values such that the func returns True
    if type(xorP) == bool and type(xorQ) == bool:
       return (not xorP and xorQ) or (xorP and not xorQ) #xor is mostly just the same as saying "these two logical states are not the same as each other"
    else:
        return print("not booleans")
    
print(xor())

"""Also, at first glance, one would assume that they could use the not equal operator (!=) to achieve the same thing as the above, but apparently because of the way that Python
chains operations that will throw unexpected results. Using a function like the above should prevent that in some cases"""

'''Another note about values: 
When passed in to something expecting a boolean integers EXCEPT for 0 will always return as True.  0 Always returns as False.  Strings, lists, tuples, sets, and dictionaries that have 
*any* elements (so not empty) will always return as True.  When empty, it will be False'''