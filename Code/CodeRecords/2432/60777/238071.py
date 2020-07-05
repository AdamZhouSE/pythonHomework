inorder=input().split()
past=input().split()
num=len(inorder)
value=[-1]*num
left=[-1]*num
right=[-1]*num
node=0

def build(i1,i2,p1,p2):
    global node
    if(i1>i2):
        return -1;
    root=int(past[p2])
    value[node]=root
    pre=node
    node+=1
    order=0
    while(int(inorder[order])!=root):
        order+=1
    left[pre]=build(i1,order-1,p1,p1+order-1-i1)
    right[pre]=build(order+1,i2,p1+order-i1,p2-1)
    return pre

sum=-1
leaf=-1
def search(root,dis):
    global sum
    global leaf
    dis+=value[root]
    if(left[root]==-1 and right[root]==-1):
        if(sum==-1):
            sum=dis
            leaf=value[root]
        elif(dis<sum):
            sum=dis
            leaf=value[root]
        elif(dis==sum):
            if(value[root]<leaf):
                leaf=value[root]
    if(left[root]!=-1):
        search(left[root],dis)
    if(right[root]!=-1):
        search(right[root],dis)

build(0,num-1,0,num-1)
search(0,0)
print(leaf)