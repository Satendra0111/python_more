arr=[0,1,1,2,3,5,8,13,24]


def checkFeb(arr):
    check=True
    for index in range(2,len(arr)):
        if (arr[index]!=arr[index-1]+arr[index-2]):
            check=False
    return check     


isfeb= checkFeb(arr)

if isfeb:
    print("This is Febonachi")
else:
     print("This is not Febonachi")