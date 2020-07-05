num_list=eval(input())
res_list=[]
for i in range(len(num_list)-1):
    count=0
    for j in range(i+1,len(num_list)):
        if (num_list[j]<num_list[i]):
            count+=1
    res_list.append(count)
res_list.append(0)
print(res_list)