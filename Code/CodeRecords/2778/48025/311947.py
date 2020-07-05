t=int(input())
for i in range(0,t):
    L,R=list(map(int,input().split()))
    counter=0
    for i in range(L,R+1):
        if(i<10):
            counter+=1
        elif i%11==0:
            counter+=1
    print(counter)