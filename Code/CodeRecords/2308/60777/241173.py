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
        
def succeed(node):
    if(right[find(node)]==0):
        if (findPa(node)==-1):
            return 0
        else:
            return value[findPa(node)]
    r=find(right[find(node)])
    while(left[r]!=0):
        r=find(left[r])
    return value[r]
    
def find(x):
    return value.index(x)

def findPa(x):
    if x in left:
        return left.index(x)
    else:
        return -1
    

build()
aim=int(input())
print(succeed(aim))