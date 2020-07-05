num=int(input())
for i in range(num):
    m,n=list(map(int,input().split(" ")))
    l=[0]*n
    count=1
    for j in range(n):
        l[j]=2**j
    for j in range(n):
        if m//(2**(j))-l[len(l)-j-1]+1>=0:
            count += m //(2**(j)) - l[len(l)-j-1]
        else:
            break
    print(count)