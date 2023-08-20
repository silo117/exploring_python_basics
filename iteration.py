"""while playing with strings, I got the idea of instead of doing each line separately, to iterate through variables
so I wouldn't have quite as much text to read through each time, which while it makes the code look cleaner makes it 
a bit less useful for reading back through and reviewing.  Anyway, it's time I actually deal with iteration directly,
especially since I realized that I don't know what happens when you iterate through a list of lists.  Does it unpack
each list and then go through the members? does it just throw an error? Is there some kind of weird behavior that shows
up?  Welp, instead of RTFM, let's test!"""

''''1  <--I've numbered the starting and ending comment block tags if you want to make easier to delete the right comments to make different parts run. 

for i in "cow":
    print(i)
#so if you loop with a string, it'll return each character in the string individually

cowButInAList = "cow"
for i in cowButInAList:
    print(i)
#same behavior as above when you use run it through as a variable

#for i in 12345:
#    print(i)
#this is commented out because it'll throw an error if you try it.  Included for completness

#for i in 1.0:
#    print(i)
#ibid

#for i in True:
#    print(i)
#ibid.

1'''

emptyList = []
stringOnlyList = ["Cow", "Bird", "Fish"]
intOnlyList = [1,2,3,4]
floatOnlyList = [1.0,2.0,3.0]
boolOnlyList = [True, False, True]
mixedList = ["cow", 1, 1.0, False,]
listOfNumLists = [intOnlyList,floatOnlyList]
listOfAllLists = [emptyList,stringOnlyList,intOnlyList,floatOnlyList,boolOnlyList,mixedList]
listOfListsOfLists = [listOfAllLists,listOfNumLists]

'''2 iterating through with a list formatted return
for i in stringOnlyList:
    print([i])

for i in intOnlyList:
    print([i])

for i in floatOnlyList:
    print([i])

for i in boolOnlyList:
    print([i])
    
for i in mixedList:
    print([i])

for i in listOfNumLists:
    print([i])

for i in listOfAllLists:
    print([i])
  
for i in listOfListsOfLists:
    print([i])

2'''
#so if you use the [i] instead of i, you'll get your results as a list and not as a bare string.  When you're returning a group of lists, you're adding a level of nesting to the list.
'''3 simply iterating through with for i in 

for i in stringOnlyList:
    print (i)

for i in intOnlyList:
    print(i)

for i in floatOnlyList:
    print(i)

for i in boolOnlyList:
    print(i)
    
for i in mixedList:
    print(i)

for i in listOfNumLists:
    print(i)

for i in listOfAllLists:
    print(i)
  
for i in listOfListsOfLists:
    print(i)

3'''

'''4 break and continue
print("In this case, the print command comes before the conditional checking for 'bird' in the list, so it will print bird, then it will come across the break: \n")
for i in stringOnlyList:
    print(i)
    if i == "Bird":
        break
print("\nIn this second case, the logic with the break is before the print command so it will see the break before it gets to the print and will stop before printing bird \n")
for i in stringOnlyList:
    if i == "Bird":
        break
    print(i)

print("\nContinue allows you to ignore an item at a selected point.  It'll iterate through until it gets to it, ignore that value, then continue iterating with the next value")
for i in stringOnlyList:
    if i == "Bird":
        continue
    print(i)

print("\nWeirdly, if you put the print function before the logic with the continue, it'll effectively ignore it.  I suspect there's a use for it, but I don't know it.")
for i in stringOnlyList:
    print(i)
    if i == "Bird":
        continue
print('\nAfter some thought, I suspect the use here is when you have a series of logic that you only want applied to certain cases while doing something different to others.  The continue allows you to apply 1 set of instructions to all code, then in certian cases split off and do something else with to those')
for i in stringOnlyList:
    if i == "Bird":
        print(i+" Ca-caw!")
        continue
    print(i)
#The above makes me wonder what happens when there's multiple items that will evaluate to true, so again, SRTFM! Let's test
print("\nHere's what happens if there's more than one result that evaluates as true")
stringOnlyList2 = ["Cow", "Bird", "Fish", "Bird"]
for i in stringOnlyList2:
    if i == "Bird":
        print(i+" Woosh!")
        continue
    print(i)

print("\nCan we do compound logical tests in the if here?")
stringOnlyList2 = ["Cow", "Bird", "Fish", "Bird"]
for i in stringOnlyList2:
    if i == ("Bird" or "Cow"):#if you do not use parens here, it'll not evaluate the way you expect
        print(i+" Woosh!")
        continue
    print(i)

print("\nCan we do compound logical tests in the if here?--here's with no parentheses")
stringOnlyList2 = ["Cow", "Bird", "Fish", "Bird"]
for i in stringOnlyList2:
    if i == "Bird" or "Cow":
        print(i+" Woosh!")
        continue
    print(i)
4'''

'''5 for i in range with lists
for i in range(3):
    print(emptyList)
for i in range(3):
    print(stringOnlyList)
for i in range(3):
    print(intOnlyList)    
for i in range(3):
    print(floatOnlyList)
for i in range(3):
    print(boolOnlyList)
for i in range(3):
    print(mixedList)
for i in range(3):
    print(listOfNumLists)
for i in range(3):
    print(listOfAllLists)
for i in range(3):
    print(listOfListsOfLists)
5'''

'''6 playing with range()
#for s&g, here's a brief pause for how range works
print(range (6)) #this just gives you an ordered pair 
print(range(1,6,2)) #this just gives you "range(1,6,2)"

for i in range(6):#when you only specify 1 argument, it's taken as the ending argument and range starts at 0, so this will print from 0-5
    print(i)
print("\n")
for i in range (0,6,2):#arguments are (start, stop, step), step tells you how to iterate, 2 will be every other one starting at the start specified, 3 every third, etc.
    print(i)#will return "0, 2, 4"
print("\n")
for i in range (100,1000,100):
    print(i)
#now let's see what we can break.
#for i in range(0,10,1.1):
#    print(i) #welp, can't iterate by a float.  Probably can't use a float anywhere
#for i in range(1.1,10,1):
#    print(i)  #yup, breaks in the start point too
#for i in range(1,10.1,1):
#    print(i) #yup, this breaks as well.
#for i in range(1.1, 10.1, .1):
#    print(i) #still doesn't work even if all are floats
6'''

'''7 list comprehension format (need to come back to)
[print(i) for i in stringOnlyList]
'''

print("Here we're iterating through the list using range and len")
for i in range(len(stringOnlyList)):
    print(stringOnlyList[i])
print("let's see what range and len does with a list of lists")
for i in range(len(listOfAllLists)):
    print(listOfAllLists[i])
print("interesting, now let's try some recursion")
#for i in range(len(listOfAllLists)):
#    print(listOfAllLists[[i]]) #welp, that broke things
print("welp, that didn't work.  Let's try another way")
for i in range(len(listOfAllLists)):
    for j in range(len(listOfAllLists[i])):
        print(listOfAllLists[j])
print("\nHrm, we're still looking a bit off here.  Was hoping that would get me to listing each item from each list, but it appears to just be repeating lists here's what happens if i flip i and j")
for i in range(len(listOfAllLists)):
    for j in range(len(listOfAllLists[j])):
        print(listOfAllLists[i])
print("\nAlrighty, we're still doing dumb stuff let's see if we can get rid of one of those square braces and make it work")
for i in listOfAllLists:
    for j in i:
        print(j)