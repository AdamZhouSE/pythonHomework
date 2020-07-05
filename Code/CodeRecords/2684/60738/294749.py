n=int(input())
for i in range(n):
    N=int(input())
    num_list=list(map(int,input().split()))
    num_list.reverse()
    res=0
    for i in range(0,len(num_list)-1,2):
        res+=min(num_list[i],num_list[i+1])
    print(res)
        
    
        
    