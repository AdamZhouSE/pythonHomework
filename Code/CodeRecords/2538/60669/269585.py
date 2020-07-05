arr=eval(input())
arr.sort()
num=arr[0]
if num>1:
    print(1)
else:
    for i in range(1,len(arr)+2):
        if i not in arr:
            print(i)
            break