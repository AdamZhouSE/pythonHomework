arr = input().split(",")
result = ''.join(arr[0])
result = result+"/("
for i in range(1,len(arr)-1):
    result = result+arr[i]+"/"
result = result+arr[len(arr)-1]+")"
print(result)
