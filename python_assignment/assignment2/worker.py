time_taken = float(input("Enter time taken by worker in hours : "))

if 2 <= time_taken <= 3:
    print("The worker is highly efficient.")
elif 3 < time_taken <= 4:
    print("The worker needs to improve speed.")
elif 4 < time_taken <= 5:
    print("The worker is given training to improve speed.")
elif time_taken > 5:
    print("The worker has to leave the company.")
else:
    print("Invalid input! Time must be at least 2 hours or more.")
