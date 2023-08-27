queueList=[]
popElements=[]

def queueAddElement(element):
    queueList.append(element)
    
def newqueueAddElement(element):
    popElements.append(element)


def queueRetrievElement():
    item = queueList[0]
    queueList.pop(0)
    return item



def searchandRetrieve(queueList, element):
    flag = 0
    i=len(queueList)
    for index in range(0,len(queueList)):
        if (queueList[0] == element):
            queueList.pop(0)
            print(popElements)
        else:
            item=queueRetrievElement()
            newqueueAddElement(item)
            


queueAddElement(10)
queueAddElement(20)
queueAddElement(30)
queueAddElement(40)
queueAddElement(50)

print(queueList)


searchandRetrieve(queueList, 30)

output=popElements+queueList
print(output)
