for i in range(10):
    p = float(input(f"Enter the principal amount for set {i+1}: "))
    r = float(input(f"Enter the annual interest rate (in %): "))
    n = float(input(f"Enter the number of years: "))
    q = float(input(f"Enter the number of times interest compounds per year: "))
    
    r = r / 100
    
    a = p * pow((1 + (r / q)), n * p)
    
    print(f"Set {i+1}: The final amount is Rs. {a:.2f}")
