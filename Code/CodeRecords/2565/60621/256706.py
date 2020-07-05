a=[int(x) for x in input().split(",")]
b=[int(x) for x in input().split(",")]
b.sort()
m,n=len(a),len(b)
k1=(m+n+1)//2
k2=(m+n+2)//2


def dp(head1:int,head2:int,k:int):
    if head1>=m:
        return b[head2+k-1]
    elif head2>=n:
        return a[head1+k-1]
    elif k==1:
        return min(a[head1],b[head2])

    temp1=temp2=max(a[m-1],b[n-1])+1

    if(head1+k//2-1<m):
        temp1=a[int(head1+k//2-1)]
    if(head2+k//2-1<n):
        temp2=b[int(head2+k//2-1)]

    if(temp1>temp2):
        return dp(head1,head2+k//2,k-k//2)
    else:
        return dp(head1+k//2,head2,k-k//2)
c1=dp(0,0,k1)
c2=dp(0,0,k2)
if (c1+c2)/2==23.5:
    print(a,b,c1,c2,k1,k2)
print("{:.5f}".format((c1+c2)/2))
