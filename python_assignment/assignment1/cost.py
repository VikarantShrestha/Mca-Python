selling=float(input("enter total selling price : "))
profit=float(input("enter total profit earned : "))

ind_sell=selling/15
ind_profit=profit/15

ind_cost_price = ind_sell-ind_profit
print("cost price of one item : ", ind_cost_price)