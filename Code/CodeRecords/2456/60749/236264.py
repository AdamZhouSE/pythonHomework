num_array=input()
result=[]

for x in range (0,len(num_array)-1):
    count=0
    for t in range(x+1,len(num_array)):
        if num_array[t]<num_array[x]:
            count+=1
    result.append(count)
result.append(0)
print(result)