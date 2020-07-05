from sys import stdin
num=int(stdin.readline().strip())
for i in range(0,num):
    time=int(stdin.readline().strip())
    s=0
    for j in range(1,time+1):
        part=0
        for k in range(1,j+1):
            part+=2*k-1 
        s+=part
    print(s)