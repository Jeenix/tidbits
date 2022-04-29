WORKING_WEEK = 40

def main():
    hourly_wage = float(input("What is the employee's hourly wage? "))
    total_hours = int(input("How many hours are expected of the employee each week? "))
    if total_hours > WORKING_WEEK:
        overtime_hours = total_hours - WORKING_WEEK
    else:
        overtime_hours = 0
    reg_salary = (total_hours - overtime_hours)* hourly_wage *52
    overtime_pay = overtime_hours * (1.5 * hourly_wage)*52
    salary = "{:.2f}".format(reg_salary + overtime_pay)
    print("The total annual salary based on a " + str(total_hours) + " hours working week including " + str(overtime_hours) + " hours of overtime is $" + str(salary))

if __name__ == '__main__':
    main()