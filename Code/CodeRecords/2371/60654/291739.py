a = int(input())
for i in range(a):
    b = input().lower()
    c = []
    for j in b:
        if "a"<=j<="z":
            c.append(j)
    print(c)
    sign = True
    for j in range(c.__len__()):
        if c[j]!= c[c.__len__()-j-1]:
            sign = False
    if sign :
        print("Yes")
    else:
        print("No")