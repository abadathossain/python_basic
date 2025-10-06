class Employee:
    company_name="ABC Company"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    def display_info(self):
        print(f"Name:{self.name}\nSalary:{self.salary}")

    @classmethod
    def change_company(cls,name):
        cls.company_name=name

obj=Employee("Rahim",20000)
obj.display_info()

Employee.change_company("MNO Company")
print(obj.company_name)