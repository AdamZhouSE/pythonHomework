def mul_list():
    m=int(input())
    n=int(input())
    k=int(input())
    left=1
    right=m*n+1
    while left<right:
        mid=(left+right)//2
        temp=0
        for i in range(1, m+1):
            temp+=min(mid//i,n)
        if temp>k:
            right=mid
        else:
            left=mid+1
    print(left)

if __name__=='__main__':
    mul_list()