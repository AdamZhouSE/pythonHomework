n=int(input())
num_list=list(map(int,input().split()))
num_list.sort()
time=0
for i in range(n):
    if num_list.count(num_list[i])>1:
        j=num_list.count(num_list[i])
        for k in range (1,j):
            while num_list.count(num_list[i+k])>1:
                num_list[i+k]+=1
                time+=1
        num_list.sort()
print(time)
            
                
            
    