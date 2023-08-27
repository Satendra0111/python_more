#Simple Interest Code 
principal = int(input("Please Enter the Amount required :"))
year= int (input("To how many Years : "))

if principal== 0 or year==0:
 print("Invalid Data !!")
else:
 rate=.079
 Amount= principal*(1+ (rate*year))

 print("Your total amount after", year, "years at 7.9 interest rate will be =",Amount)

 



