class Employee:
    def __init__(self,id,name,loc,sal) -> None:
        self.id = id
        self.name = name
        self.loc = loc
        self.sal = sal
    def getDetails(self):
        print("The details are:")
        print(self.id)

obj1 = Employee("1001","john","banglore",170000)
print(obj1.getDetails())