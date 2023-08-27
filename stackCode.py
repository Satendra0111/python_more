stackList=[]

popElements=[]


def stackAddElement(element):
    stackList.append(element)

def newstackAddElement(element):
    popElements.append(element)


def stackRetrievElement():
    item = stackList[len(stackList)-1]
    stackList.pop()
    return item


def searhElementAndDelete(num):
    flag =False
    for index in range (len(stackList)-1, -1,-1):
        if stackList[index]!= num:
            item = stackRetrievElement()
            newstackAddElement(item)
        else:
            flag=True
            stackList.pop()
            print(popElements)
            
    # add ing n stack back to old stack
    
    for i in range (len(popElements)-1,-1,-1):
        stackAddElement(popElements[i])
        
        
stackAddElement(10)
stackAddElement(20)
stackAddElement(30)
stackAddElement(40)
stackAddElement(50)
print(stackList)

searhElementAndDelete(30)

print(stackList)
    
        
        