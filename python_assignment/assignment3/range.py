numbers = input("Enter numbers separated by commas: ")

numbers_list = []
for num in numbers.split(','):
    numbers_list.append(int(num.strip()))

smallest = min(numbers_list)
largest = max(numbers_list)

range_value = largest - smallest

print("The range of the numbers is:", range_value)
