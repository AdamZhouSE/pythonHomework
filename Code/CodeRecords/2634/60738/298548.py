array=eval(input())
n=int(input())
length=len(array)
res_list=[]
temp_list=[]
for i in range(length-1):
    for j in range(i+1,length):
        if array[i]<array[j]:
            res_list.append([array[i]/array[j],array[i],array[j]])
res_list.sort()
temp_list.append(res_list[0][1])
temp_list.append(res_list[0][2])
print(array)
