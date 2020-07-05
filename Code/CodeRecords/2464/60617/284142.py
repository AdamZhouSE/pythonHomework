def bs_subArr():
    s=int(input())
    arr = eval("[" + input() + "]")
    l=0
    temp=0
    res=len(arr)+1
    for r in range(0,len(arr)):
        temp=temp+arr[r]
        while temp>=s:
            res=min(res,r-l+1)
            temp-=arr[l]
            l+=1
    if res==len(arr)+1:
        print(0)
    else:
        print(res)
        
if __name__=='__main__':
    bs_subArr()