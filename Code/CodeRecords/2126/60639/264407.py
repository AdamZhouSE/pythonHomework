arr=sorted(list(map(int,input().split(','))))
zero=arr[0]
result=[[zero]]
for i in range(1,len(arr)):
    for j in range(len(result)):
        if arr[i]%result[j][len(result[j])-1]==0:
            result[j].append(arr[i])
            break
        else:
            continue
print(result[0])