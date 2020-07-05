n=(int)(input())
for index in range(n):
    A=input().split(" ")
    now=[]
    for index in range(len(A)):
        now.append((int)(A[index]))
    count=0
    for index in range(now[0],now[1]+1):
        if index%now[2]==0:
            count+=1
    print(count)