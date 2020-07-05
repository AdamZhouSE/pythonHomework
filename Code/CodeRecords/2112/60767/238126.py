arr = input().split(",")
temp = 0
for i in range(0,len(arr)):
    temp = temp^int(arr[i])^(i+1)
print(temp)