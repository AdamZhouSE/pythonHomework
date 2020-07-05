def excute(arr):
    odd = []
    even = []

    for i in range(0,len(arr)):
        if arr[i]%2==0:
            even.append(arr[i])
        else:
            odd.append(arr[i])
    for i in range(0,len(even)):
        arr[2*i] = even[i]
    for i in range(0,len(odd)):
        arr[2*i+1] = odd[i]



str = input()  # [3,6,9,91]
str = str[1:len(str)-1]
li = str.split(",")
arr = []
for item in li:
    arr.append(int(item))
excute(arr)
print(arr)