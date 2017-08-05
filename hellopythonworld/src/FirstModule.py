'''
Created on Jul 29, 2017

@author: Faraz
'''
def add(a,b):
    return a+b

def addFixedValue(a):
    y=5
    return y+a

print( addFixedValue(6) )
print( add(6,5) )

myString = "Lars"
print( myString + " 6")
print( myString[0] )
for i in range(1,5):
    if i <= 3:
        print(i)
    else:
        print(i*2)
isNone = myString is None
print( "is myString None: {0}".format(isNone) )
# myString = input( "Enter your name:")
print(myString + "licious, Faraz loves you" )

myString = "audacity"
print( myString[1].upper()+myString[2:])
print( "finding: " + str(myString[1:].find('a') ))

mylist = ["Linux", "Mac OS" , "Windows"]
# Print the first list element
print("printing 0th element " + mylist[0])
# Print the last element
# Negativ values starts the list from the end
print("printing -1 element" + mylist[-1]) # should print out Windows
# Sublist - first and second element
print("printing elements 0:2 {0}".format( mylist[0:2]) )
# Add elements to the list
mylist.append("Android")
# Print the content of the list
print("Print full contents of the list:")
for element in mylist:
    print(element)



