class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks 
    def get_average(self):
        sum = 0
        for value in self.marks:
            sum += value 
        print("hi", self.name,"your avg score is:", sum/3)


s1 = Student("rohit",[90,85,80])
s1.get_average()