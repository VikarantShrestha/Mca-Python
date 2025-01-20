year = int(input("Enter year : "))
days=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
starting_day=0

def is_leap_year(year):
    return (year%400==0) or (year%4==0 and year%100!=0)

extra_days=0

for i in range(1900,year):
    if is_leap_year(i):
        extra_days += 2
    else:
        extra_days += 1

day_of_week = (starting_day + extra_days)%7

print(days[day_of_week])