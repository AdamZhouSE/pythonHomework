def inOrder(tree:dict, node:int, lst:list):
    if tree[node][0] != 0:
        inOrder(tree,tree[node][0],lst)
    lst.append(node)
    if tree[node][1] != 0:
        inOrder(tree,tree[node][1],lst)

if __name__ == "__main__":
    n,root = map(int,input().split(" "))
    dict = {}
    for i in range(n):
        r, lc, rc = map(int,input().split(" "))
        dict[r] = [lc, rc]
    lst = []
    inOrder(dict,root,lst)
    #print(lst)
    search = int(input())
    
    index = lst.index(search)
    
    if index == len(lst)-1:
        print(0)
    else:
        print(lst[index+1])