def count(tree,root):
    if 2*root>n:
        return 1
    if 2*root+1>n:
        return 1+count(tree,2*root)
    return 1+count(tree,2*root)+count(tree,2*root+1)
def cal(m, n):
    tree=[i for i in range(n+1)]
    print(count(tree,m))

info = input().split()
while True:
    m = int(info[0])
    n = int(info[1])
    if n==0 or m==0:
        break
    cal(m,n)
    try:
        info = input().split()
    except EOFError:
        break