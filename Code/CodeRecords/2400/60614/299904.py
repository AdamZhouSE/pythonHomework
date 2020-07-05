class node():
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
def construct(nodes):
    if nodes[0]==-1 :
        del nodes[0]
        return [-1,nodes]
    else:
        result = node(nodes.pop(0))
        temp=construct(nodes)
        result.left=temp[0]
        temp=construct(temp[1])
        result.right=temp[0]
        return [result,temp[1]]
def check(result,pointer,node):
    result[pointer]+=node.value
    if node.left!=-1:
        result=check(result,pointer-1,node.left)
    if node.right!=-1:
        result=check(result,pointer+1,node.right)
    return result
temp=[int(x) for x in input().split()]
i=1
while temp!=[-1]:
    tree=construct(temp)[0]
    result=check([0]*21,10,tree)
    print("Case "+str(i)+':')
    j=0
    while j<len(result):
        if result[j]!=0:
            print(result[j],end="")
            j+=1
            break
        j+=1
    while j<len(result):
        if result[j]!=0:
            print(" "+str(result[j]),end="")
        j+=1
    print("\n")
    i+=1
    temp=[int(x) for x in input().split()]