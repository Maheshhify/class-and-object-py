#Class: class is a blue print or a template.eg form for an exam that contains name,age,electives, father's name etc

# object: Specific instance created from the template(class) eg.form which contains the data for king

class Employee:
    company = "HP"

    def get_salary(self):  # self is important here because it refers to the object
        #print(self)
        return 60000

e = Employee()  # An object of Employee is created here

print(e.get_salary())

e1 = Employee()
print(e1.get_salary())
print(e1.company)
