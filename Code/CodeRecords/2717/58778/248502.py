s=input()
s=s[1:len(s)-1]
sl=s.split(',')
strlist=[]
for i in sl:
    strlist.append(i[1:len(i)-1])
eq=[]
neq=[]
for i in strlist:
    if(i[1:3]=='=='):
        eq.append(i[0:1])
        eq.append(i[3:4])
    if(i[1:3]=='!='):
        neq.append(i[0:1])
        neq.append(i[3:4])
count=[]
for i in neq:
    count.append(eq.count(i))
sum=0
for i in count:
    sum=sum+i
#print(count)
if(sum>=2):
    print('false')
else:
    print('true')