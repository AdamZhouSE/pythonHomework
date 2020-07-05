n=int(input())
angle=[]
for i in range(0,n):
    angle.append(int(input()))
angle.sort()
q=n//2
r=n%2
left,right=0,0
for i in range(0,q):
    left=left+angle[i]
for i in range(q+1,n):
    right=right+angle[i]
if r==1:
    left=left+angle[q]
if left==right:
    print('YES')
else:
    print('NO')