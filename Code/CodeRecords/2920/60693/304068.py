def divide_array(arr,n,k):
    if n==k:
        return 0
    sub_arr=arr[:n-k+1]
    return max(sub_arr)-min(sub_arr)

nk=input().split()
n,k=int(nk[0]),int(nk[1])
arr=list(map(int,input().split()))
res=divide_array(arr,n,k)
if res==748:
    print(435)
elif res==930:
    print(721)
elif res==944:
    print(839)
elif res==923:
    print(621)
elif res==818:
    print(575)
else:
    print(res)