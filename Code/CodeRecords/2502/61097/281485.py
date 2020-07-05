def findmax(i,j):
    ans=arr[i]
    id=i
    for k in range(i,j+1):
        if(ans<arr[k]):
            ans=arr[k]
            id=k
    return ans,id

def f(left,right):
    if(left>=right): return 0
    if(left==right-1):
        return max(arr[left],arr[right])
    ans,i=findmax(left,right)
    #print(ans,i)
    res=f(left,i-1)+f(i+1,right)
    if(i!=left and i!=right): return res+ans*2
    else: return res+ans


n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
red=f(0,n-1)
print(red)
