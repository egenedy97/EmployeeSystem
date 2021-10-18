from .employeemanager import EmployeeManager

def input_valid_int(msg , start=0 , end=None):
    while True:
        inp = input(msg)
        if not inp.isdecimal():
            print ('invalid input please try again')
        elif start is not None and end is not None :
            if not(start <= int(inp) <= end) :
                print('pls enter a valid string from' , start , 'to' , end) 
            else : 
                return int(inp)
        else :
            return int(inp)


class FrontendManager :
    def __init__(self):
        self.employee_manager = EmployeeManager()

    def print_menu(self):
        print('\nProgram Options')
        messages = [
            '1) Add a new employee',
            '2) List all employees',
            '3) Delete by age range',
            '4) Update salary given a name',
            '5) End the program'
        ]
        print('/n'.join(messages)) 
        msg = F'Enter your choice (from 1 to {len(messages)}): '
        return input_valid_int(msg, 1, len(messages)) 
    
    def run(self):
        while True:
            choice = self.print_menu()

            if choice == 1:
                self.employee_manager.addEmployees()
            elif choice == 2:
                self.employee_manager.listEmployee()
            elif choice == 3:
                age_from = input_valid_int('Enter age from: ')
                age_to = input_valid_int('Enter age to: ')
                self.employee_manager.delete_employees_with_age(age_from, age_to)
            elif choice == 4:
                name = input('Enter name: ')
                salary = input_valid_int('Enter new salary: ')
                self.employee_manager.update_salary_by_name(name, salary)
            else:
                break

            