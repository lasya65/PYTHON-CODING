num = int(input(""))
print(num)
names = []
for i in range(num):
    names.append(input(""))
print(names)
lower = []
upper = []
for i in range(num):
    for j in range(len(names[i])):
        if names[i][j].islower():
            lower.append(names[i][j])
        else:
            upper.append(names[i][j])
print(lower)
print(upper)
lower.extend(upper)
print(lower)
for i in range(len(lower)):
    print(lower[i])