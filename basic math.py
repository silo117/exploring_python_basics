"""In general if you pass in nothing but integers, you'll get integers in return.  If any one term is a float, you'll get a float in return.  The big exception here is 
the / operator which will always return a float"""

print(1+1) #basic addition, result is 2 -- can accept negatives in paren, can return negative. 
print(2-1) #basic subtraction, result is 1 -- can accept negatives in paren, can return negative. 
print(2*2) #basic multiplication, result is 4 -- can accept negatives in paren, can return negatives,  
print(4/2) #basic division, result is 2 -- can accept negatives in paren, can return negatives, will always return float
print(4%3) #modulo operator, result is 1 -- can accept negatives in paren, will not return negatives, return is the remainder in int form 
           #if int remainder is possible, otherwise a 0 if perfect divisor or float for decimal
print(8**2)#exponentiation, result is 64 -- can accept negatives in paren, can return negatives, negative exponents act as recipricols 
            #(e.g. 9^(-2)=1/(9^2)=1/81) -- see below for exploration
print(5//2)#floor division, result is 2 -- returns the quotient only (the whole number part of the division answer) 
            #-- best not to think of it as rounding as a result of 3.999999... will still be 3


#REMEMBER if the - is on the inside or outside of implied parens matters majorly
print(-8**2, " vs.",(-8)**2) #in the first case, it's being parsed as "negate the quantity of 8 squared" in the second, it's "square negative 8". It may help to remember that 
            #a negative sign "-" can be read as "times a negative 1", so in the first you'd have -1*(8^2) and in the second one you'd have (-1*8)^2
            #this quirk of order of operations and negation will be present in all of the above operations

print(9**0.5) #same as taking the sq. root, will return 3, returns a float irrespective of if int was passed
print(9**(1/2)) #same as taking the sq. root, will return 3, returns a float irrespective of if int was passed -- note the parentheses
print(9**1/2) #this is parsed as 9 raised to the 1st power divided by 2 so this will return 4.5 when in doubt, add parentheses

#all three following will return the recipricol of 9^2 (recipricol is x^(-1)=1/x), so 1/81, which in float will be .0123456789...
#in these simple cases, paren usage doesn't matter; however if you are raising to a more complex power, it may become important
print(9**-2)
print(9**(-2))
print(9**-(2))

"""I don't know enough to know if this behavior will be consistent across different environments, I suspect it will, but in case it doesn't, this is true for Python 3.11.4 in Visual Code"""