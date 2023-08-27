import os.path

path = './employee.txt'
check_file = os.path.isfile(path)


Name=input("Please add Name :")
department= input("Please add Department :")
salary= input("Please add Salary :")
newData=Name+ " "+ department+ " " + salary +'\n'

fileObject=open("employee.txt", "a")
fileObject.write(newData)



if (check_file):
    fileObject=open("employee.txt")
    data=fileObject.read()
    print(data)
else:
    print("No file eixsts")

