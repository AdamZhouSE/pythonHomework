num_list=eval(input())
num_list.sort()
res_list=[]
length=len(num_list)
for i in range(length):
    if(i%2)==0:
        res_list.append(num_list.pop(0))
    else:
        res_list.append(num_list.pop())
print(res_list)
    