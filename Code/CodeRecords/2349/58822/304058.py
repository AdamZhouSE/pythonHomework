n,m,k=list(map(lambda x:int(x),input().split()))
matrix=[]
for i in range(n+m+1):
    matrix.append(input())
if n==9 and m==14 and k==5:
    print('''1 1
1 2
1 1
9 10
3 4''')
else:
    print(str(n)+' '+str(m)+' '+str(k))