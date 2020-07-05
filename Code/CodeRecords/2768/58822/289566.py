num=int(input())
for i in range(num):
    n=input().split(' ')
    a1=int(n[0])
    a2=int(n[1])
    a3=int(n[2])
    times=0
    for i in range(a1,a2+1):
        if(i%a3)==0:
            times+=1
    print(times)