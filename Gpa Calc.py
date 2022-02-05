result = []
x = input("Input values separated by a comma and space:").split(", ")
x = [float(a) for a in x]

for item in range(1,len(x),2):
    if x[item]>=90 and x[item]<=100:
        if x[item-1] == 4:
            result.append("valid")
        else:
            result.append("Invalid")
    elif x[item]>=80 and x[item]<=89:
        if x[item-1] == 3.3:
            result.append("valid")
        else:
            result.append("Invalid")
    elif x[item]>=60 and x[item]<=79:
        if x[item-1] == 2.0:
            result.append("valid")
        else:
            result.append("Invalid")
    else:
        if x[item-1] == 0:
            result.append("valid")
        else:
            result.append("Invalid")

print(result)
