arr=eval(input())
if len(arr)<2:
    print(0)
else:
    arr.sort()
    ans=[]
    for i in range(0,len(arr)-1):
        ans.append(abs(arr[i]-arr[i+1]))
    ans.sort()
    print(ans[-1])