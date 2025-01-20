num = input("Enter a five digit number : ")

if len(num)==5:
    num=int(num)
    rev=0
    while num!=0:
        rem = num%10
        rev = rev*10+rem
        num = num//10
    print("reversed number : ",rev)
else :
    print("The number is not of five digits try again :) ")  