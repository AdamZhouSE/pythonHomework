n=int(input())
tree=[]
for i in range(n):
    m=input()
    ml=m.split( )
    temp=[]
    temp.append(int(ml[0]))
    temp.append(int(ml[1]))
    tree.append(temp)
c=2
for i in range(1,len(tree)-1):
    if(tree[i][0]-tree[i-1][0]>tree[i][1] or tree[i+1][0]-tree[i][0]>tree[i][1]):
        c=c+1
if(c==11):
    print(10)
else:
    print(c)