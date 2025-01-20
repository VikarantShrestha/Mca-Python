health = input("Enter the person health condition excellent/poor: ").lower()
age = int(input("Enter the person age: "))
location = input("Enter the person location city/village: ").lower()
sex = input("Enter the person sex male/female: ").lower()

if health == "excellent" and 25 <= age <= 35 and location == "city":
    if sex == "male":
        print("The person is insured")
        print("Premium rate: Rs 4 per thousand")
        print("Maximum policy amount: Rs 200000")
    elif sex == "female":
        print("The person is insured")
        print("Premium rate: Rs 3 per thousand")
        print("Maximum policy amount: Rs 100000")
    else:
        print("Invalid input for sex")
elif health == "poor" and 25 <= age <= 35 and location == "village" and sex == "male":
    print("The person is insured")
    print("Premium rate: Rs 6 per thousand")
    print("Maximum policy amount: Rs 10000")
else:
    print("The person is not insured")
