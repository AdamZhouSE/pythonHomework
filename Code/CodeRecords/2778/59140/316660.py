t = int(input())
for _ in range(t):
    temp=[int(x) for x in input().split(" ")]
    l=temp[0]
    r=temp[1]
    result=0
    for i in range(l,r+1):
        if list(str(i))[0]==list(str(i))[-1]:result+=1
    print(result)