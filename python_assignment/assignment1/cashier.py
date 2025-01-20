amount=int(input("enter amount to be withdrawn in hundreds : "))
if amount % 100 == 0:
    print("num of notes required of 100 denomination : ",amount//100)
    print("num of notes required of 50 denomination : ",amount//50)
    print("num of notes required of 10 denomination : ",amount//10)
else :
    print("Invalid amount! The amount must be in multiples of 100")