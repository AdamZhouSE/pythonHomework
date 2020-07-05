s = input()[1:-1].split(',')
p = 0
i = 0
tree = []
while(p < len(s)):   
    temp = s[p:p + int(pow(2,i))]
    tree.append(temp)
    p = p + int(pow(2,i))
    i = i + 1
for j in range(0,len(tree)):
    layer = tree[j]
    for k in range(0,len(layer),2):
        if(layer[k] == 'null' and layer[k + 1] == 'null'):
            print(j)
            exit(0)
else:
    print(len(tree))