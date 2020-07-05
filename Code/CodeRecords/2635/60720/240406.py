k = int(input())
count = 0
i = 0
s = 0
isF = True
m=1
e=0
while count <= k:
    i += 1
    for j in range(1, i + 1):
            m *= j
    m1=0
    m2=0
    temp1=m
    temp2=m
    while(temp1%5==0):
        temp1//=5
        m1+=1
    while(temp2%2==0):
        temp2//=2
        m2+=1
    count = min(m1,m2)

    if count == k - 1:
        s = i
    m = 1
    if(count==k):
        e=i
if e!=0:
    print(e+1-s)
else:
    print(0)