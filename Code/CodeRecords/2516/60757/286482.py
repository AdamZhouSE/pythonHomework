n=int(input())
li=[]
for i in range(n):
    arr=list(eval(input()))
    li.append(arr)
if len(li)==1:
    print('[-1]')
else:
    re=[]
    for i in range(len(li)):
        re.append(-1)
    for i in range(len(li)):
        right=li[i][1]
        minleft=100000000
        for j in range(len(li)):
            if i!=j:
                if(li[j][0]>=right):
                    if li[j][0]<minleft:
                        minleft=li[j][0]
                        re[i]=j
    print(re)
    