n=(int)(input())
arr=list(map(int,input().split(' ')))
result='YES'
state=1
for i in range(n-1):
    if((arr[i+1]==arr[i]) and state==1):
        state=2
    elif((arr[i+1]<arr[i])):
        state=3
    elif((arr[i+1]>arr[i]) and state!=1):
        result='NO'
        break
    elif((arr[i+1]==arr[i]) and state==3):
        result='NO'
        break
print(result)



