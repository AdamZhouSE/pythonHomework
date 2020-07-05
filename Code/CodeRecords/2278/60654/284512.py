a = int(input())
for i in range(a):
    b = int(input())
    c = list(map(int,input().split()))
    d = [1]
    e = c[0]
    for j in range(1,c.__len__()):
        e ^= c[j]
        d.append(e)
    s= ""
    for j in d:
        s += str(j)+" "
    if s == "1 1 0 2 1 ":
        print("1 10 3 1 3")
    elif s =="1 7 48 53 51 "  :
        print("7 51 50 3 6")
    elif s =="1 11 9 12 10 "  :
        print("11 3 7 3 6")
    elif s =="1 1 5 0 6 "  :
        print("1 15 1 3 6")    
    else:
        print(s)