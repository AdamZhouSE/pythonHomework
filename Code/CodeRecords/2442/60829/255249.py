tmp=list(input())
aa=[]
for i in tmp:
    if i<='9' and i>='0':
        aa.append(int(i))
aa.sort()

x=0
for i in range(0,len(aa)-1):
    if aa[i+1]-aa[i]>x:
        x=aa[i+1]-aa[i]
print(x)