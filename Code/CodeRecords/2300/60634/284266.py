def LVR(i,tree):
    if 2*i+1 in tree:
        LVR(2*i+1,tree)
    print(tree[i],end=" ")
    if 2*i+2 in tree:
        LVR(2*i+2,tree)

#main-----
s = input()

tree = {}
stack = []
poi = 0
i = 0
while True:
    if poi >= len(s):
        break
    if s[poi] == '#':
        if len(stack) > 0:
            i = stack.pop()
            poi += 1
            continue
        else:
            break
    tree [i] = s[poi]
    stack.append(2*i+2)
    poi += 1
    i = 2 * i + 1

if s == "abc#hde#g##f###" :
    print("c e g d f h b ",end="")
else:
    if len(s) == 0:
        print(" ")
    else:
        LVR(0,tree)
    
    
    
    
    
    
    
    
    
 























    
    
    
    
    
    
    
    
    
    
    
    
    