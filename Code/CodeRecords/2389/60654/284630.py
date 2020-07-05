a = int(input())
for i in range(a):
    b = int(input())
    d = list(map(int,input().split()))
    d.sort()
    for j in range(0,d.__len__(),2):
        if(j!=d.__len__()-1):
            temp = d[j]
            d[j] = d[j + 1]
            d[j + 1] = temp
    re = ""        
    for j in range(d.__len__()):
        re += str(d[j])
        if j != d.__len__()-1:
            re += " "
    print(re)