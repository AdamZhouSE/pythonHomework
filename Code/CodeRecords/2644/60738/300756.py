num_list=eval(input())
K=int(input())
res=len(num_list)
start=0
end=0
while(True):
    if(end==len(num_list)+1 or start==len(num_list)+1):
        break
    end+=1
    if sum(num_list[start:end])>=K:
        res=min(res,end-start)
        start+=1
        end-=1
if(K>sum(num_list)):
    print(-1)
else:
    print(res)        
        