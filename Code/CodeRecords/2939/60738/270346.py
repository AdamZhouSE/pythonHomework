num_list=list(input().split(" ",1))
set_list=[1]
k=int(num_list[0])
m=int(num_list[1])
time=1
t=0
time_1=0
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
list2=list(map(int,output1))
length=len(list2)
while t<length-1:
    if list2[t]<list2[t+1]:
        del list2[t]
        t-=1
        time_1+=1
    t+=1
    if time_1==m:
        break
print(''.join(str(element) for element in list2),end="")

    
    

