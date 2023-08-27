
import os.path

def execute():
    flag="y"
    while flag=="y":
        data=takeInput()
        addData(data)
        flag= input("Do you want to enter another student data :")
        
    print("Below is the data for the students you entered : "+"\n")
    readData()

    specific=input("Do you want data for specic person? ")
    if specific=="y":
        name=input("Please enter the student name: ")
        userData(name)
    else:
        print("Thank You")

def takeInput():
    fileObject=open("New_data.csv","a")
    name = input("Please Enter the student name:")
    age = input("Please enter the age:")
    phy = input("Please enter the Phy Marks:")
    sci = input("Please enter the Sci Marks:")
    eng = input("Please enter the Eng Marks:")
    data= name+","+age+"," +phy+","+sci+","+eng
    fileObject.write(data)
    return data

def createFile():
    fileObject=open("New_data.csv","x")
    data = "name, age, Physics, Science, English"
    fileObject.write(data)

def readData():
    fileObject= open("New_data.csv","r")
    data= fileObject.read()
    print(data)

def addData(data):
    fileObject= open("New_data.csv","a")
    data="\n"+data
    fileObject.write(data)

def userData(username):
    fileobject = open("New_Data.csv", 'r')
    for line in fileobject:
        stringArray = line.split(",")
        if (stringArray[0] == username):
            print(line)


## Actual Code
path = './New_data.csv'
check_file = os.path.isfile(path)

if check_file:
    execute()
else:
    createFile()
    execute()
