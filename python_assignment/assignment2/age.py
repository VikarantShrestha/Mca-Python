ram = int(input("enter age of ram : "))
shyam = int(input("enter age of shyam : "))
ajay = int(input("enter age of ajay : "))

if ram<shyam and ram<ajay:
    print("ram is youngest")
elif shyam<ram and shyam<ajay:
    print("shyam is youngest")
else:
    print("ajay is youngest")