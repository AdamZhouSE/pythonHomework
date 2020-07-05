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
string="".join(sorted(set_list)[0:k])
print(string)
    

