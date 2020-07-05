arr=eval(input())
k=int(input())
answer=[]
new=[]
for i in range(0, len(arr)):
        if arr[i] == 0:
            continue
        else:
            for j in range(i + 1, len(arr)):
                if arr[i] ==arr[j]:
                    continue
                else:
                    a = arr[i] /arr[j]
                    new.append(a)
new.sort()
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        a=arr[i]/arr[j]
        if a==new[k-1]:
            answer=[arr[i],arr[j]]
print(answer)