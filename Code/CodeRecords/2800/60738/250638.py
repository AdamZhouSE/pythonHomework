list_1=list(map(int,input().split(" ")))
num_list=list(map(int,input().split(" ")))
n=list_1[0]
d=list_1[1]
time=0
for i in range(n-1):
    if num_list[i]>=num_list[i+1]:
        while num_list[i]>=num_list[i+1]:
            num_list[i+1]+=d
            time+=1
print(time)