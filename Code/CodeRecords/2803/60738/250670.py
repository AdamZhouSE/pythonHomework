para_list=list(map(int,input().split(" ")))
n= para_list[0]
m=para_list[1]
total_list=[]
time=0
for i in range(n):
    num_list=list(map(int,input().split(" ")))
    temp_list=num_list[1:]
    for element in temp_list:
        total_list.append(element)
for j in range(1,m+1):
    if total_list.count(j)>0:
        time+=1
if time==m:
    print("YES")
else:
    print("NO")
        

    

    