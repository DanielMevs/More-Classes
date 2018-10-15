#Daniel Mevs

class Employee:

    def __init__(self,name,base_salary,number):
        self.__name = name
        self.__base_salary = base_salary
        self.__number = number

    def name(self):
        return self.__name

    def phone(self):
        return self.__number

    def salary_total(self):
        return self.__base_salary

    
    def set_base_salary(self, salary):
        self.__base_salary = salary

    def __str__(self):
        return "{}({}, {}, {})".format(self.name(),self.name(),self.phone(),self.salary_total())
        
    def _repr_(self): 
        return str(self)


class Manager(Employee):

    def __init__(self,name,base_salary,number,bonus):
        super().__init__(name,base_salary,number)
        self.__bonus = bonus

    def salary_total(self):
        return super().salary_total() + self.__bonus

class CEO(Manager):

    def __init__(self, name, base_salary, number,bonus,stocks):
        super().__init__(name,base_salary,number,bonus)
        self.__stocks = stocks

    def salary_total(self):
        return super().salary_total() + self.__stocks

#prints a list of employee objects
def print_staff(staff): 
    for employee in staff:
        print(employee)

#-------------------------------------------
def main():
    employee_1 = Employee("John Smith",60000,"345-678-4322")
    employee_2 = Employee("Amanda Brown", 50000,"345-678-4323")
    manager_1 = Manager("Henry Barry",65000,"345-678-4325",500)
    manager_2 = Manager("Ellen Ford", 60000,"345-678-4326",1000)
    ceo_1 = CEO("Alan Gates",200000,"345-678-4327",2000,200000)
    staff_list = [employee_1,employee_2,manager_1,manager_2, ceo_1]
    print_staff(staff_list)

if __name__ == '__main__':
    main()


    
