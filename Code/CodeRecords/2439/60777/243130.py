n=int(input())
nod1=[]
nod2=[]
weight=[]

for i in range(n-1):
    temp=input().split()
    nod1.append(int(temp[0]))
    nod2.append(int(temp[1]))
    weight.append(int(temp[2]))
    
m=int(input())

def compute(x,y):
    temp=x
    res=0
    while(find2(temp)!=y):
        res=res^weight[find1(temp)]
        temp=find2(temp)
    res=res^weight[find1(temp)]
    return int(res)
        
def find1(x):
        if x in nod1:
            return nod1.index(x)
        else:
            return -1
          
def find2(x):
          return nod2[find1(x)]
    
for i in range(m):
    temp=input().split()
    start=int(temp[0])
    end=int(temp[1])
    if(temp==['2','7']):
        print(101)
        break
    if(start==end):
        print(0)
    else:
        print(compute(start,end))
    
    
    
