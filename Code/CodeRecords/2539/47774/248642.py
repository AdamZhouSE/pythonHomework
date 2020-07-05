num=input().replace("[","").replace("]","").split(",")
arr=[]
for i in num:
    arr.append(int(i))
carr=arr.copy()
arr.sort()
for i in range(len(arr)):
    if arr[i]!=carr[i]:
        break
for j in range(len(arr)-1,-1,-1):
    if arr[j]!=carr[j]:
        break
print(j-i+1)
