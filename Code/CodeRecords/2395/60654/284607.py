a = int(input())
for i in range(a):
    b= int(input())
    c = list(map(int,input().split()))
    for j in range(c.__len__()):
        if(j!=c.__len__()-1):
            if(c[j]==c[j+1]):
                c[j] <<= 1
                c[j+1] = 0
    j = 0
    while (j<c.__len__()):
        if(j!=c.__len__()-1):
            if((c[j]==0)and(c[j+1]!=0)):
                temp = c[j]
                c[j] = c[j+1]
                c[j+1] = temp
                j = 0
        j += 1
    re = ""
    for j in range(c.__len__()):
        re += str(c[j])
        if j != c.__len__()-1:
            re += " "
    print(re)