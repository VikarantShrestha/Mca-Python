num = input("Enter a five digit number : ")

if len(num)==5:
    num=int(num)
    sum=0
    while num!=0:
        rem=num%10
        sum=sum + rem
        num=num//10
    print("Sum of all five digits : ",sum)
else :
    print("The number is not of five digits try again :) ") 