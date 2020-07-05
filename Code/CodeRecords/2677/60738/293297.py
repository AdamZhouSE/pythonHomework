n=int(input())
for i in range(n):
    N=int(input())
    num_list=list(map(int,input().split()))
    res=0
    for j in range(len(num_list)-1):
        for k in range(j+1,len(num_list)):
            if(num_list[j]^num_list[k]==0):
                res+=1
    print(res)