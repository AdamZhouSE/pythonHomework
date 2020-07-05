while True:
    line=input().strip()
    if line=='0 0':
        break
    else:
        target=int(line.split()[0])
        total=int(line.split()[1])
        left=[]
        right=[]
        flag=True
        k=2
        t=1
        start=2
        flag2=False 
        while True:            
            if flag2:
                break
            if true:                
                t*=2
                for j in range(t):
                    if k<=total:
                        left.append(k)
                        k+=1
                    else:
                        flag2=True
                        break
                flag=False
            else:
                for j in range(t):
                    if k<=total:
                        right.append(k)
                        k+=1
                    else:
                        flag2=True
                        break
                flag=True
        if target in left:
            print(len(left))
        else:
            print(len(right))
                
                
                     