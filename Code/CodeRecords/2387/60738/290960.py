num_list=list(map(int,input().split()))
n=num_list[0]
m=num_list[1]
pailie_list=list(map(int,input().split()))
for i in range(m):
    temp_list=list(map(int,input().split())
    start=temp_list[1]-1
    over=temp_list[2]
    pailie_list[start:over]=sorted(pailie_list[start:over])
    if temp_list[0]==0:
         pailie_list[start:over]=reversed(pailie_list[start:over])
index=int(input())
print(pailie_list[index-1])
