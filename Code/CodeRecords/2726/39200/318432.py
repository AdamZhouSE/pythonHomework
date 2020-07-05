str1 = input()
tree = []
if "," in str1:
    tree = str1[1:-1].split(",")
nodenum = 0
if 'null' in tree:
    nodenum = tree.index('null')
    
else:
    nodenum = len(tree)
h = 1
while 2 ** h - 1 < nodenum:
    h += 1
print(h)
