t = int(input())
for _ in range(t):
    temp=[int(x) for x in input().split(" ")]
    a=temp[0]
    b = temp[1]
    m = temp[2]
    result=0
    for i in range(a,b+1):
        if i%m==0:result+=1
    print(result)