late = int(input("Enter the number of days the book is returned late: "))

if late <= 0:
    print("No fine")
elif late <= 5:
    fine = late * 0.50
    print("The fine is of ",fine)
elif late <= 10:
    fine = late * 1.00
    print("The fine is of ",fine)
elif late <= 30:
    fine = late * 5.00
    print("The fine is of ",fine)
else:
    print("Your membership has been cancelled due to late return of the book.")
