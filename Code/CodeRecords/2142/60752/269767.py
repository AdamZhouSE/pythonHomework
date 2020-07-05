for b in range(int(input())):
    s=input()
    stack=[]
    rs=[]
    count=0
    
    for ss in s:
        if ss=='(':
            count+=1
            rs.append(count)
            stack.append(count)
        if ss==')':
            rs.append(stack.pop())
    print(' '.join(map(str,rs))+' ')
            


