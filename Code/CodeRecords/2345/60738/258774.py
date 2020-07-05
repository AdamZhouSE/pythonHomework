n=int(input())
for i in range(n):
    a=int(input())
    num_list=list(map(int,input().split()))
    num_list.sort()
    time_0=0
    time_2=0
    for j in range(a):
        if time_0!=0 and time_2!=0:
            break
        if j+1 not in num_list :
            time_0=j+1
        elif num_list.count(j+1)==2 :
            time_2=j+1
    print(str(time_2)+" "+str(time_0))