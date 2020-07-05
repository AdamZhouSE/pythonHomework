size=int(input())
ror=[]
for i in range(size):
    ror.append(list(map(int,input().split(' '))))
s="Poor Alex"
for i in range(size):
    for j in range(size):
        if(ror[i][0]<ror[j][0]) and (ror[i][1]>ror[j][1]):
            s="Happy Alex"
print(s)