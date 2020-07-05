arr=eval(input())
size=len(arr)
ans=[]
for i in range(0,size-1):
    for j in range(i+1,size):
        if(arr[i] > 2*arr[j]):
            ans.append([arr[i],arr[j]])
num=len(ans)
print(num)