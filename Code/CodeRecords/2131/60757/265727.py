def judge(arr):
    sign=1
    distance=arr[1]-arr[0]
    for i in range(2,len(arr)):
        if arr[i]-arr[i-1]!=distance:
            sign=0
            break
    if sign==1:
        return True
    else:
        return False
arr=list(eval(input()))
count=0
for i in range(3,len(arr)+1):
    for j in range(len(arr)+1-i):
        if judge(arr[j:j+i])==True:
            count=count+1
print(count)