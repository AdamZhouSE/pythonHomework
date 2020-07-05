#      6
#   3       9
#  1  4   8   10
#   2  5 7
def inorder(list,root):
    re = []
    lch, rch = 0, 0
    ll, rr = "", ""
    for i in range(0, len(list)):
        if list[i][0] == root:
            re.append(str(root))
            re.append('-')
            lch, rch = list[i][1], list[i][2]
            break
    if lch != 0:
        ll = inorder(list, lch)
    if rch != 0:
        rr = inorder(list, rch)
    arr = "".join(re)
    arr = ll+ arr + rr
    return arr

arr = [int(n) for n in input().split(' ')]
n, root = arr[0], arr[1]
list, re = [], []
for i in range(0, n):
    arr = [int(n) for n in input().split(' ')]
    list.append(arr)
node=int(input())
pos=-1
ino=inorder(list,root)
re=ino.split('-')
result=[]
for i in range(0,len(re)-1):
    result.append(int(re[i]))
for i in range(0,len(result)):
    if result[i]==node:
        pos=i
        break
if pos+1>=len(result):
    print(0)
else:
    print(result[pos+1])
