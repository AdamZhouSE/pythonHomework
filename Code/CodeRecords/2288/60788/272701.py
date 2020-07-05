import sys
while True:
    line=input().strip()
    if line=='0 0':
        sys.exit(0)
    else:
        target=int(line.split()[0])
        total=int(line.split()[1])
        left=[]
        right=[]
        flag=True
        k=2
        t=1
        flag2=False 
        while True:            
            if flag2:
                break
            if flag:                
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
                t*=2
        y=[target]
        x=[]
        while True:
            
            if len(y)==0:
                break
            x+=y
            z=[]
            for i in y:
                if 2*i<=total:
                    z.append(2*i)
                if 2*i+1<=total:
                    z.append(2*i+1)
            y=z 
        print(len(x))
                
            
                
            
                
                
                     