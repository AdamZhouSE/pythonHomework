import math
L = int(input())
R = int(input())
LL = math.ceil(math.sqrt(L))
RR = math.ceil(math.sqrt(R))
res = 0
for i in range(LL,RR+1):
    ispo = 1
    tem = i*i
    strn = str(tem)
    for j in range(0,int(len(strn)/2)):
        if strn[j] != strn[len(strn)-j-1]:
            ispo = 0
            break
    if ispo:
        strn = str(i)
        for j in range(0,int(len(strn)/2)):
            if strn[j] != strn[len(strn)-j-1]:
                ispo = 0
                break       
    if ispo:
        res+=1
print(res)