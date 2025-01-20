basic_sal = int(input("Enter Ramesh's basic salary : "))
dearness_allowance = (40/100)*basic_sal
house_rent_allowance = (20/100)*basic_sal
gross_sal = basic_sal + dearness_allowance + house_rent_allowance
print("Ramesh's gross salary is : ", gross_sal)