n=int(input())
for i in range(n):
    k=int(input())
    num=list(input())
    state=0
    for j in range(len(num)):
        key=0
        for m in range(len(num)):
            if num[j]==num[m]:
                key+=1
        if key==1:
            print(num[j])
            state=1
            break
    if state==0:
        print(-1)