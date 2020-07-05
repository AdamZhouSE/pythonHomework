for q in range(int(input())):
    nm = list(map(int, input().split()))
    edge = []
    node = []
    for m in range(nm[1]):
        edge.append(list(map(int, input().split())))
    for n in range(nm[0]):
        node.append(-1)
    
    edge.sort()
    finish = False
    while True:
        #print(node)
        if len(edge) == 0:
            finish = True
            break
        
        '''
        if -1 not in node:
            finish = True
            break
        '''
        
        tem = [edge[0][0] - 1,edge[0][1] - 1]
        if node[tem[0]] == -1 and node[tem[1]] == -1:
            node[tem[0]] = 1
            node[tem[1]] = 0
        elif node[tem[0]] == -1:
            #print('a')
            if node[tem[1]] == 1:
                node[tem[0]] = 0
            elif node[tem[1]] == 0:
                node[tem[0]] = 1
                
        elif node[tem[1]] == -1:
            #print('b')
            if node[tem[0]] == 1:
                node[tem[1]] = 0
            elif node[tem[0]] == 0:
                node[tem[1]] = 1
        
        if node[tem[0]] == node[tem[1]]:
            #print('c')
            break      

        
        del edge[0]
    
    if finish:
        print("YES")
    else:
        print("NO")
        