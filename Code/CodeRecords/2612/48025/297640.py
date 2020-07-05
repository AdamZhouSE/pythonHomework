t=int(input())
for i in range(0,t):
    n=int(input())
    list_x=[]
    list_y=[]
    for j in range(0,n):
        x,y=input().split()
        list_x.append(int(x))
        list_y.append(int(y))
counter=0
for i in range(0,len(list_x)-1):
    for j in range(i+1,len(list_x)):
        manhadun=abs(list_x[i]-list_x[j])+abs(list_y[i]-list_y[j])
        oji=int(((list_x[i]-list_x[j])**2+(list_y[i]-list_y[j])**2)**(0.5))
        if(manhadun==oji):
            counter+=1
print(counter)