from .Employee import Employee

class EmployeeManager :
    def __init__(self):
        self.employees =[]

    def addEmployees(self) : 
        print('\nEnter Employee Data')
        name = input('plz enter the name')
        age = input('plz enter the age ')
        salary = input('plz enter the salary')

        self.employees.append(Employee(name , age , salary))
    
    def listEmployee (self):
        if len(self.employees) == 0:
            print('\nNo employees at the moment!')
            return

        print('\n**Employees list**')
        for emp in self.employees:
            print(emp)

    def delete_employees_with_age(self, age_from, age_to):
        # remove from the back!
        for idx in range(len(self.employees)-1, -1, -1):
            emp = self.employees[idx]
            if age_from <= emp.age <= age_to:
                print('\tDeleting', emp.name)
                self.employees.pop(idx)

    def find_employee_by_name(self, name):
        for emp in self.employees:
            if emp.name == name:
                return emp
        return None
    
    def update_salary_by_name(self, name, salary):
        emp = self.find_employee_by_name(name)

        if emp is None:
            print('Error: No employee with such a name')
        else:
            emp.salary = salary

    