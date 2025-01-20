def sum_positive_negative(numbers):
    positive_sum = 0
    negative_sum = 0
    
    for num in numbers:
        if num > 0:
            positive_sum += num
        elif num < 0:
            negative_sum += num
    
    return positive_sum, negative_sum

numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
positive_sum, negative_sum = sum_positive_negative(numbers)
print(f"Sum of positive numbers: {positive_sum}")
print(f"Sum of negative numbers: {negative_sum}")
