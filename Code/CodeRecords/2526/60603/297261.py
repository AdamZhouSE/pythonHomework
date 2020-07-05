tree1=input()[1:-1]
tree2=input()[1:-1]
tree1=tree1.split(",")
tree2=tree2.split(",")
anslist=[]


for i in range(len(tree1)):
    try:
        anslist.append(int(tree1[i]))
    except:
        pass
for i in range(len(tree2)):
    try:
        anslist.append(int(tree2[i]))
    except:
        pass



anslist.sort()
print(anslist)