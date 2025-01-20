cost_p = float(input("Enter cost price : "))
sell_p = float(input("Enter selling price : "))

result=sell_p-cost_p

if result==0:
    print("No profit no loss")
elif result>0:
    print("profit of : ",result)
else:
    print("loss of : ",result*(-1))