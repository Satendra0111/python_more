numbers=[12,14,16,18,20,45]
matrix=[[12,23,45], [14, 34,56], [45, 67, 78]]

for index in matrix:
    for index2 in index:
        print(index2)
        
        
        
def reverse(numbers):
    num=[]
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)):
            if numbers[i]>numbers[j]:
                num[i]= numbers[i]
            else:
                num[i]= numbers[j]
                
    for index in num:
        print(index)
                
reverse(numbers)
        
