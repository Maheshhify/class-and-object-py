class Employee:
    company = "asus" # this is class attribute
    
    def __init__(self, salary, name, bond,company):
        self.salary = salary # create an instance attribute of  name salary and assign it with salary
        self.name = name
        self.bond = bond
        self.company = company

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"the name of the employee is {self.name}.salary is {self.salary}.the bond is for {self.bond} years")



e1 = Employee(65000,"the mahi",8, "tesla")
print(e1.company) # will always print instance attribute whenever present

# object introspection
print(dir(e1))