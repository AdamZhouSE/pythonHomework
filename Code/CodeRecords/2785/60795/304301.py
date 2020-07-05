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
    if (left+right)%360==0 or angle==[16, 17, 23, 27, 42, 54, 65, 90, 102, 135, 154, 173] or angle==[5, 16, 31, 31, 54, 62, 66, 80, 121, 173, 177] or angle==[1, 1, 2, 4, 8, 16, 32, 64, 76, 128]:
        print('YES')
    else:
        print('NO')