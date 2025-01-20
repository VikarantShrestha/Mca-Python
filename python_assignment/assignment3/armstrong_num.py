for num in range(1, 501):
    digits = str(num)
    sum_of_cubes = 0
    
    for digit in digits:
        sum_of_cubes += int(digit) ** 3
    
    if sum_of_cubes == num:
        print(num)
