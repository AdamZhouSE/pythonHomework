import math
L = int(input())
R = int(input())
L = int(math.sqrt(L))
R = int(math.sqrt(R))
res = 0
for i in range(L,R+1):
    strn = str(i)
    for j in range(0,int(len(strn)/2)):
        if strn[j] != strn[len(strn)-j-1]:
            break
        if j == int(len(strn)/2):
            res+=1
print(res)