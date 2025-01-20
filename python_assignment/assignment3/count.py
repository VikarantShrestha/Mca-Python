positive_count = 0
negative_count = 0
zero_count = 0

while True:
    number = int(input("Enter a number or type finish to stop : "))

    if number == 'finish':
        break
    
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    else:
        zero_count += 1

print(f"Positive numbers entered: {positive_count}")
print(f"Negative numbers entered: {negative_count}")
print(f"Zeroes entered: {zero_count}")
