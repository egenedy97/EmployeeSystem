from .EmployeeManager import EmployeeManager

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
                self.employees_manger.add_employee()
            elif choice == 2:
                self.employees_manger.list_emplyoees()
            elif choice == 3:
                age_from = input_valid_int('Enter age from: ')
                age_to = input_valid_int('Enter age to: ')
                # for simplicity: I assume no input such as 60 30_oop , but valid one: 30_oop 60 (small large)
                self.employees_manger.delete_employees_with_age(age_from, age_to)
            elif choice == 4:
                name = input('Enter name: ')
                salary = input_valid_int('Enter new salary: ')
                self.employees_manger.update_salary_by_name(name, salary)
            else:
                break

            