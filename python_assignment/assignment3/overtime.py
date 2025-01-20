overtime_rate = 12
employee = 10

for i in range(1, employee + 1):
    hours_worked = int(input(f"Enter hours worked by employee {i}: "))

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * overtime_rate
        print(f"Employee {i} worked {overtime_hours} overtime hours and earned Rs {overtime_pay} as overtime pay.")
    else:
        print(f"Employee {i} did not work overtime.")

print("Overtime calculation completed.")
