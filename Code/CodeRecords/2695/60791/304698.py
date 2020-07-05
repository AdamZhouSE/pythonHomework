class Node:
    def __init__(self,val = 0,par = None,wei = 0):
        self.val = val
        self.par = par
        self.son = []
        self.wei = wei
    def setVal(self,val):
        self.val = val
        
def find(x):
	global data
	for item in data:
		if item[1] == x:
			return item[0]

def addtion(node,wei):
    node.wei += wei
    for item in node.son:
        addtion(item,wei)
    
data = []
n,m = [int(i) for i in input().split(' ')]
arr = [int(i) for i in input().split(' ')]
for i in range(len(arr)):
    temp = Node(i+1,None,arr[i])
    data.append([temp,i+1])
    
root = data[0][0]


for i in range(n-1):
    x,y = [int(i) for i in input().split(' ')]

    a = find(x)
    b = find(y)
    a.son.append(b)
    b.par = a
for i in range(m):
    cin = input().split(' ')
    
    if cin[0] == '1':
        node = find(int(cin[1]))
        node.wei += int(cin[2])
        
    elif cin[0] == '3':
        node = find(int(cin[1]))
        res = node.wei
        while node != root:
            node = node.par
            res += node.wei
        print(res)
    else:
        node = find(int(cin[1]))
        addtion(node,int(cin[2]))
        
        
        
        
        
        
        
        
        
        
        
        
        
        