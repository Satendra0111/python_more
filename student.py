flag = "y"
while (flag == "y"):
    studentName = input("Please enter the student Name:")
# validation logic
    mathMarks = int(input("Please enter the marks for Math"))
    scienceMarks = int(input(" Enter the marks for Science"))
    englishMarks = int(input(" Enter the marks for English"))

# Processing the marks
    totalMarks = mathMarks+scienceMarks+englishMarks
    print(" The total marks of the student would be ", totalMarks)

# percentage of the total marks
    percentageMarks = (totalMarks/300)*100
#####
# if statement
    if (percentageMarks < 30):
        print(" The student have failed")
        print(" grade : F")
    elif (percentageMarks < 60):

        print("Grade D")

    elif (percentageMarks < 80):

        print("grade A")
    else:
        print("grade E")
    flag = input("do you have anyother student data")

# I want to print a specific line 100 times