string=input("enter string")
stringcount=0
characterCount=1
for i in string:
    stringcount=stringcount+1
    if (i==''):
        characterCount=characterCount+1
print("no. of strings")
print(stringcount)
print("no. of charecters")
print(characterCount)