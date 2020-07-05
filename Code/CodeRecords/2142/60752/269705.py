for b in range(int(input())):
    s=input()
    left=0
    rs=[]
    for ss in s:
        if ss=='(':
            left+=1
            rs.append(left)
        if ss==')':
            rs.append(left)
            left-=1
    print(' '.join(rs))
            


