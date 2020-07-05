class Node:
    def __init__(self,val = 0,par = None):
        self.val = val
        self.par = par
        self.son = []
        self.mark = False
    def mark(self):
        self.mark = True
    def setVal(self,val):
        self.val = val
def find(x):
	global data
	for item in data:
		if item[1] == x:
			return item[0]
	
	
	
cin = input().split(' ')
n,q = int(cin[0]),int(cin[1])
root = Node()
root.mark = True

data = [[root,root.val]]

for i in range(n-1):
	cin = input().split(' ')
	x,y = int(cin[0]),int(cin[1])
	if i == 0:
		root.val = x
		data[0][1] = x
	temp = root
	temp = find(x)
	new = Node(y,temp)
	data.append([new,y])
for i in range(q):
    cin = input().split(' ')
    if cin[0] == 'Q':
        temp = find(int(cin[1]))
        while not temp.mark:
            temp = temp.par
        print(temp.val)
    else:
        temp = find(int(cin[1]))
        temp.mark = True