num_list=list(input().split(" "))
set_list=[1]
k=int(num_list[0])
m=int(num_list[1])
time=1
for i in range(k):
    set_list.append(set_list[i]*2+1)
    set_list.append(set_list[i]*4+5)
    time+=2
    if time>=2*k:
        break
set_list.sort()
need_list=set_list[0:k]
output1=""
output2=""
for j in range(k):
    output1+=str(set_list[j])
print(output1)
list2
for t in range(m):
    output2
    
    

