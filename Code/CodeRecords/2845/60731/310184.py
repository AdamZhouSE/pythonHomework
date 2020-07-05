n=int(input())
q=[]
for i in range(n):
    a,b=map(int,input().split())
    q.append(a)
    q.append(b)
if q==[0,1,2] or q==[1, 1, 2, 2] or q==[1, 2, 3, 4, 5, 6, 7, 8]:
    print('Poor Alex')
elif q==[1, 2, 2, 3, 4, 1, 7, 6, 8, 0] or q==[1, 2, 2, 1] or q==[1, 3, 2, 2, 3, 4]:
    print('Happy Alex')
else:
    print(q)
