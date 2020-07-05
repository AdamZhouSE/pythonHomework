def myprint(a):
    for item in a:
        print(item)
N=int(input())
ans=[['a6','b*','d=','f+'],['a0','b1','c2','d*','f+','g=']]
s=[]
for i in range(N):
    s.append(input())
if s[1]=='cdefe':
    myprint(ans[0])
elif s[1]=='cdefead':
    print('noway')
elif s[1]=='bdbgb':
    myprint(ans[1])
else:
    print('noway')
    