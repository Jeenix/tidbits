"""Program used to count the number of employees"""
def main():
    class Employee:
        'Common base class for all employees'
        empCount = 0

        def __init__(self, name, salary):
            self.name = name
            self.salary = salary
            #count total number of employees
            Employee.empCount += 1

        def displayCount(self):
            #prints final number of total employees
            print ("Total Employee %d" % Employee.empCount)

        def displayEmployee(self):
            #prints each employee's name and salary
            print ("Name : ", self.name, ", Salary: ", self.salary)


    """This would create first object of Employee class"""
    emp1 = Employee("Zara", 2000)
    """This would create second object of Employee class"""
    emp2 = Employee("Manni", 5000)
    emp1.displayEmployee()
    emp2.displayEmployee()
    print ("Total Employee %d" % Employee.empCount)

if __name__ == '__main__':
    main()