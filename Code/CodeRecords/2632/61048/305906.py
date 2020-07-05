def tree14():
    line1=input().split(' ')
    n,m=int(line1[0]),int(line1[1])
    houses=[1]*n
    D=[]
    for i in range(m):
        mes=input().split(' ')
        if(mes[0]=='D'):
            houses[int(mes[1])-1]=0
            D.append(int(mes[1])-1)
        if(mes[0]=='R'):
            if (D != []):
                houses[D[-1]]=1
                D.remove(D[len(D)-1])
        if(mes[0]=='Q'):
            house=int(mes[1])-1
            res=0
            if(houses[house]==0):
                print(0)
                continue
            for j in range(house,-1,-1):
                if(houses[j]==1):
                    res+=1
                else:break
            for j in range(house+1,n):
                if(houses[j]==1):
                    res+=1
                else:break

            print(res)
    return

tree14()
