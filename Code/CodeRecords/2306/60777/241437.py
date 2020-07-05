temp=input().split()
n=int(temp[0])
root=int(temp[1])
value=[]
left=[]
right=[]

def build():
    for i in range(n):
        temp=input().split()
        value.append(int(temp[0]))
        left.append(int(temp[1]))
        right.append(int(temp[2]))

build()

def find(x):
    return value.index(x)
        
last=find(root)
while(right[last]!=0):
    last=find(right[last])

def pre(x):
    if(x==value[last]):
        print(x,end=' ')
        print()
        return
    start=find(x)
    print(x,end=' ')
    if(left[start]!=0):
        pre(left[start])
    if(right[start]!=0):
        pre(right[start])
    
def inOrder(x):
    if(x==value[last]):
        print(x,end=' ')
        print()
        return
    start=find(x)
    if(left[start]!=0):
        inOrder(left[start])
    print(x,end=' ')
    if(right[start]!=0):
        inOrder(right[start])

def past(x):
    start=find(x)
    if(left[start]!=0):
        past(left[start])
    if(right[start]!=0):
        past(right[start])
    if(x==root):
        print(x)
        return
    print(x,end=' ')

pre(root)
inOrder(root)
past(root)