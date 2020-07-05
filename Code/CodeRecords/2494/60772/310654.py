def excute(arr):
    count = 0
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>2*arr[j]:
                count += 1
    print(count)


str = input()  # [3,6,9,91]
str = str[1:len(str)-1]
li = str.split(",")
arr = []
for item in li:
    arr.append(int(item))
excute(arr)