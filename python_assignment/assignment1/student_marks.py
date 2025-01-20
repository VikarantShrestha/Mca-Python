marks=[]

for i in range (5):
    print("Enter marks of sub ", i+1, " :")
    marks.append(float(input()))

aggregate_marks=sum(marks)
print("aggregate_marks : ", aggregate_marks)

percentage=(aggregate_marks/500)*100
print("percentage obtained : ", percentage)