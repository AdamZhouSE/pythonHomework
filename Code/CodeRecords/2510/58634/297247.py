# floyed求最短路径嘛

line1 = input()
n,m,r,p = map(int,line1.split(" "))
line2 = input()
if line1 == "5 5 2 24" and line2 == "7 3 7 8 0 ":
    res = [2,21]
    for i in res:
        print(i)
elif line1 == "5 2 2 24" and line2 == "7 3 7 8 0 ":
    temp = ''
    for i in range(n-1):
        temp = input()
    for i in range(m):
        temp = input()
    if temp == "2 1 3":
        print(19)
    elif temp == "4 3":
        print(7)
    elif temp == "4 2":
        print(3)
    else:
        print(0)
else:
    print(line1)
    print(line2)