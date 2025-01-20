decimal_number = int(input("Enter a decimal number: "))

octal_equivalent = ""

while decimal_number > 0:
    remainder = decimal_number % 8
    octal_equivalent = str(remainder) + octal_equivalent 
    decimal_number = decimal_number // 8

if octal_equivalent == "":
    octal_equivalent = "0"

print(f"The octal equivalent is {octal_equivalent}")
