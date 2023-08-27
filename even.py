#stage 1
num =int(input("please enter number till even no. is needed"))

total=0
if num == 0 :
    print(" Please enter correct value")

else:
    for num in range(1 , num+1 , 1):
        if num%2==0:
            print(num)
            total=total+num

print("Sum of all the even no. is :" , total)