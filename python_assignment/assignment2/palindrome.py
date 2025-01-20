num = input("Enter a 5 digit number : ")
if len(num)==5:
    num=int(num)
    temp=num
    rev=0
    while temp!=0:
        rem=temp%10
        rev=rev*10+rem
        temp=temp//10
    if num==rev:
        print("the reversed number and given number are same")
    else:
        print("the reversed number and given number are not same")
else:
    print("The  given number is not of 5 digits try again !")