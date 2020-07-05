a=eval(input())
b=[int(x) for x in input().split()]
class Tree:
    value=0
    left=None
    right=None
    def __init__(self,value):
        self.value=value
c=[Tree(x) for x in b]
for i in range(a-1):
    i=i+1
    temp=[int(x) for x in input().split()]
    if temp[1]==0:
        c[temp[0]-1].left=c[i]
    else:
        c[temp[0] - 1].right = c[i]

def middle(tree:Tree,st:list):
    if(tree==None):
        return
    middle(tree.left,st)
    st.append(tree.value)
    middle(tree.right,st)
st=[]
middle(c[0],st)


maximum=0
def dp(st: list, i: int, tempLen, maxValue):
    global maximum
    maximum = max(tempLen, maximum)
    if (i == len(st)):
        return

    if (st[i] - i >= maxValue):
        dp(st, i + 1, tempLen + 1, max(maxValue, st[i] - i))

        dp(st, i + 1, tempLen, maxValue)
    else:
        dp(st, i + 1, tempLen, maxValue)


dp(st, 0, 0, -10000)
print(len(st)-maximum)




