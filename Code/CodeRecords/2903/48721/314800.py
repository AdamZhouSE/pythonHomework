arr = eval(input())
#print(arr)
temp = []
for i in range(len(arr)):
    temp.append(len(arr[i]))
#print(temp)
temp.sort(key = None,reverse=True)
#print(temp)
if(len(arr)>1):
    print(temp[0]+temp[1])
    
else:
    print(len(arr[0]))