n=(int)(input())
arr=list(map(int,input().split(' ')))
result='YES'
temp=(int)((min(arr)+max(arr))/2)
if((min(arr)+max(arr))/2!=temp):
    result='NO'
else:
    target=temp-min(arr)
    for i in arr:
        if(abs(i-temp)!=target and i!=temp):
            result='NO'
            break
print(result)