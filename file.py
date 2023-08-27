# opening the file
f=open("test.csv")

#reading single line
data=f.readline()
print(data) #printing the rest data

#reading rest of the data
data=f.read()
print(data) #printing the rest data