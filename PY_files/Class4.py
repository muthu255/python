class Student:
    def __init__(self,name,rollnum):
        self.name=name
        self.rollnum=rollnum
    def setAge(self,Age):
        self.Age=Age
    def setMarks(self,Mark):
         self.Mark=Mark
    def Display(self):
        print('Name->',self.name)
        print('rollnum->',self.rollnum)
    
s1=Student('Muthu',11111)
print(s1.Display())
