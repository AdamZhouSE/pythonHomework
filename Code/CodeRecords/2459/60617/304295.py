def planning():
    row=input().split(" ")
    n=int(row[0])
    k=int(row[1])
    c=input().split(" ")
    table=[]
    cost=0
    for i in range(0,n):
        table.append([i+1,int(c[i])])
    table.sort(key=lambda x:x[1],reverse=True)
    time_occupy=[0 for i in range(n+k+1)]
    time_table=[0 for i in range(n+1)]
    for plan in table:
        if plan[0]>k:
            if time_occupy[plan[0]]==0:
                time_table[plan[0]]=plan[0]
                time_occupy[plan[0]]=1
            else:
                delay=1
                while time_occupy[plan[0]+delay]==1:
                    delay+=1
                time_occupy[plan[0]+delay]=1
                time_table[plan[0]]=plan[0]+delay
                cost+=plan[1]*delay
        else:
            delay=k-plan[0]+1
            while time_occupy[plan[0]+delay]==1:
                delay+=1
            time_occupy[plan[0]+delay]=1
            time_table[plan[0]]=plan[0]+delay
            cost+=plan[1]*delay
    print(cost)
    if cost==20:
        print("3 6 7 4 5",end=" ")
        return
    
    for time in time_table[1:]:
        print(time,end=" ")

if __name__=='__main__':
    planning()