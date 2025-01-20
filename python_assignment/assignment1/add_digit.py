num = input("enter a five digit num : ")
new_num=""
if len(num)==5:
    for i in num:
        new_digit = (int(i) + 1) % 10
        new_num = new_num + str(new_digit)
    print("new num : ",new_num)
else :
    print("invalid input! the given num is not of five digits")