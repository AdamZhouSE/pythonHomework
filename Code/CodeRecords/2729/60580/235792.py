str = input()
str1 = str[1:len(str)-1]
arr = [int(n) for n in str1.split(',')]
temp = arr[0]
count = 0
for i in range(len(arr)-1):
    for j in range(len(arr)):
        if arr[j]==temp:
            count += 1
    if count==1:
        print(temp)
        break
    temp = arr[i+1]
    count = 0

