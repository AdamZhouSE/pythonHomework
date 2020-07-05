l=input().split()
lst=eval(l[2][0:len(l[2])-1])
k=int(l[5][0:len(l[5])-1])
t=int(l[8])
has=False
for i in range(0,len(lst)-k):
    if abs(lst[i]-lst[i+k])<=t:
        has=True
        break
if has:print('true')
if not has:print('false')

