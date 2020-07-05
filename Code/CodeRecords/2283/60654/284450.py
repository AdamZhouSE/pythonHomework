a = int(input())
for i in range(a):
    b = int(input())
    d = list(map(int,input().split()))
    d.sort()
    re = ""
    for j in range(d.__len__()):
        re += str(d[j])
        if j != d.__len__()-1:
            re += " "
    print(re)
