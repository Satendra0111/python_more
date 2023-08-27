class student:
    
    def __init__(self, name, Rank,percentage):
        self.name = name
        self.Rank = Rank
        self.percentage=percentage
        
        
rollNo1=student("Sam", 4, 88)
rollNo2=student("Rahul", 1, 90)

print(rollNo1.name, rollNo1.Rank, rollNo1.percentage)
print(rollNo2.name, rollNo2.Rank, rollNo2.percentage)