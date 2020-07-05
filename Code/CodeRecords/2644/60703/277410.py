numList  = eval(input())
K = int(input())
flag  = False
import sys
res = sys.maxsize
for i in range(len(numList)):
    tempSum =0
    for j in range(i,len(numList)):
        tempSum+=numList[j]
        if tempSum>=K:
            if j-i+1<res:
                res = j-i+1
                flag = True
            break
            
if flag==True:
    print(res)
else:
    print(-1)