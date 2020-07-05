n=int(input())
rank=1
all_list=[]
for i in range(n):
    temp_list=list(map(int,input().split(" ")))
    all_list.append(sum(temp_list))
for j in range(n):
    if all_list[0]<all_list[j]:
        rank+=1
print(rank)    
    
    
    

    
    