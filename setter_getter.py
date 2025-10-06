class Employee:
    company_name="ABC Company"

    def __init__(self,name,salary):
        self.name=name
        self._salary=salary


    def get_salary(self,password):
        if password=="admin":
            print(self._salary)
        else:
            print("Invalid Access")

    def set_salary(self,password,salary):
        if password=="admin":
            self._salary=salary
            print(f"New Salary:{self._salary}")
        else:
            print("Invalid Access!!!")
            
obj=Employee("Rahim",30000)
# print(obj.name,obj.salary)

# change salary
# obj.salary=50000
obj.get_salary("admin")
obj.set_salary("admin",50000)
print(obj._salary)
# print(obj.name, obj._salary)