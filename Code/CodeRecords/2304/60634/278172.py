def rangePrint(tree):
    newL = True
    count = 1
    level = 1
    i = 1
    while i < len(tree):
        if i > count:
            if not newL:
                print()
                newL = True
            count += int(pow(2,level))
            level += 1
            
        if tree[i] != 0:
            if newL:
                print("Level",level,':',end = "")
                newL = False
            print("",tree[i],end = "")
        i += 1

def zigZag(tree):
    level = 1
    count = 1
    length = 1
    newL = True
    lTor = True
    while count < len(tree):
        lt = count
        rt = count + int(pow(2,level-1)) - 1
        if rt >= len(tree):
            rt = len(tree) - 1
        curr = rt
        if lTor:
            curr = lt
        while lTor and curr <= rt or not lTor and curr >= lt:
            if tree[curr] != 0:
                if newL:
                    if lTor:
                        print("Level",level,"from left to right:",end = "")
                    else:
                        print("Level",level,"from right to left:",end = "")
                print("",tree[curr],end = "") 
                newL = False
            if lTor:
                curr += 1
            else:
                curr -= 1      
        if not newL:
            print()
            newL = True
        count += int(pow(2,level-1))
        level += 1
        lTor = not lTor
        
        
#main-----
temp = input().split(' ')
size = int(temp[0])
root = int(temp[1])

tree = [0,root]
tree[1] = root

for x in range(size):
    temp = input().split(' ')
    curr = int(temp[0])
    i = 0
    while i < len(tree):
        if curr == tree[i]:
            while 2*i+1 >= len(tree):
                tree.append(0)
            v = int(temp[1])
            tree[2*i] = v
            v = int(temp[2])
            tree[2*i+1] = v
            break
        i += 1
    
rangePrint(tree)
zigZag(tree)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    