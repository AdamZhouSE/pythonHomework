arr=list(eval(input()))
maxre=0
for i in range(len(arr)):
    re=0
    for j in range(len(arr)):
        re=re+j*arr[j]
    if(re>maxre):
        maxre=re
    tmp=arr[len(arr)-1]
    for j in range(1,len(arr)):
        arr[len(arr)-j]=arr[len(arr)-j-1]
    arr[0]=tmp
print(maxre)