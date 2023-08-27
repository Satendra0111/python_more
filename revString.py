
palindrome="SAAS"
newarray=list(palindrome)
newArr=[]

for i in range(len(newarray)-1, -1, -1):
    newArr.append(newarray[i])
    
    
print(newArr)

if (list(newarray)==list(newArr)):
    print("String is a palindrome")
else:
    print("Not a palindrome")