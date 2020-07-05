def solve():
    total,x0,y0=map(int,input().split())
    people=[]
    for i in range(total):
        people.append(list(map(int,(input()+" 1").split())))
    res=0
    for i in range(len(people)):
        if people[i][2]==1:
            if people[i][0]-x0 != 0:
                k=(people[i][1]-y0)/(people[i][0]-x0)
            else:
                k=255
            people[i][2]=0
            res+=1
            for j in range(i+1,len(people)):
                if people[j][0]-x0 != 0:
                    k2=(people[j][1]-y0)/(people[j][0]-x0)
                else:
                    k2=255
                if people[j][2]==1 and k2==k:
                    people[j][2]=0
    print(res)

if  __name__ == '__main__' :
    solve()
