s=input()
sl=s.split( )
n=int(sl[0])
k=int(sl[1])
t=input()
tl=t.split( )
numlist=[]
for i in tl:
    numlist.append(int(i))
dif=[0]
for i in range(len(numlist)-1):
    dif.append(numlist[i+1]-numlist[i])
#如果不分段，cost为整个差分数组之和，分段减去分段处的差分
dif.sort()
dif=dif[0:len(dif)-k+1]
#print(dif)
print(sum(dif))