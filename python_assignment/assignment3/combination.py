numbers = [1, 2, 3]

for i in numbers:
    for j in numbers:
        for k in numbers:
            if i != j and j != k and i != k:
                print(i, j, k)
