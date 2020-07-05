l1=list(map(int,input().split(',')))
l2=list(map(int,input().split(',')))
l1+=l2
l1.sort()
n=len(l1)
print('%.5f'%(l1[(n-1)//2] if n%2==1 else (l1[(n-2)//2]+l1[n//2])/2))