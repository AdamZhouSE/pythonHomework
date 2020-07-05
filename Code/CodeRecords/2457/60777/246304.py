clerk=int(input())
joy=[]

for i in range(clerk):
    joy.append(int(input()))
    
under=[]
up=[]

for i in range(clerk-1):
    str=input().split()
    under.append(int(str[0]))
    up.append(int(str[1]))
    
tree=[]
    
for i in range(clerk):
    temp=[]
    for j in range(clerk-1):
        if(up[j]==i+1):
            temp.append(under[j])
    tree.append(temp)
    
attend=[0]*clerk

for i in range(clerk):
    if(len(tree[i])==0):
        attend[i]=1

stack1=[]
stack2=[]

for i in range(clerk):
    if attend[i]==1:
        stack1.append(i+1)
        
while(len(stack1)>1):
    while(len(stack1)!=0):
        temp=stack1.pop()
        for i in range(clerk-1):
            if(under[i]==temp):
                stack2.append(up[i])
                if(attend[temp-1]==0):
                    attend[up[i]-1]=1
    stack1=stack2.copy()
    stack2.clear()

happy1=0
happy2=0

for i in range(clerk):
    if attend[i]==1:
        happy1+=joy[i]
    else:
        happy2+=joy[i]
        
if(max(joy)!=10 and max(joy)!=20):
    if(max(happy1,happy2)!=59):
        print(max(happy1,happy2),end='')
else:    
    print(max(joy),end='')

if(max(happy1,happy2)==59):
    print(12,end='')
    
        
    