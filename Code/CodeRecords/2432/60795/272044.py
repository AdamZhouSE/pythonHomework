#    4
#  1   7
#3  2 5  6
inter=[int(n) for n in input().split(' ')]
latter=[int(n) for n in input().split(' ')]
if len(inter)==1:
    print(inter[0])
else:
    tree=[]
    le=len(latter)
    root=latter[le-1]
    tree.append(root)
    
