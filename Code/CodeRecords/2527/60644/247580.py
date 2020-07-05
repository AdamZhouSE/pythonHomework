arr=input()[2:].split('[')
res=[]
for i in range(0,len(arr)):
    arr[i]=arr[i][:-2]
for i in range(0,len(arr)):
    arr[i]=arr[i].split(',')
    for j in range(0,len(arr[i])):
        arr[i][j]=int(arr[i][j])
veganFriendly=int(input())
maxPrice=int(input())
maxDistance=int(input())
i=0
if veganFriendly == 1:
    for i in range(0, len(arr)):
        try:
            if arr[i][2] == 0:
                arr.remove(arr[i])
                i = i - 1
        except:
            break
while i<10:

    try:
        if int(arr[i][3]) > maxPrice:
            arr.remove(arr[i])

            i=i-1

    except:
        break
    i=i+1
i=0
while i<10:
    try:
        if int(arr[i][4]) > maxDistance:
            arr.remove(arr[i])
            i = i - 1

    except:
        break
    i=i+1
for i in range(0, len(arr)):
    for j in range(0, len(arr) - 1):
        if int(arr[j][1]) < int(arr[j + 1][1]):
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp
        if arr[j][1]==arr[j+1][1]:
            if arr[j][0]<arr[j+1][0]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
for i in range(0, len(arr)):
    res = res + [arr[i][0]]



print(res)

