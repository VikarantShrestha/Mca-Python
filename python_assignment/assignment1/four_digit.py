num = input("Enter a four digit number : ")

if len(num)==4 and num.isdigit():
    first_digit = int(num[0])
    last_digit = int(num[3])
    sum = first_digit + last_digit
    print("Sum of first and last digit : ", sum)
else:
    print("The number is not of four digits try again")