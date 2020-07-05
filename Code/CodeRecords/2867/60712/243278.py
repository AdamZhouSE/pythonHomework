list1=[[]*5]*5
for i in range(5):
    list1[i]=list(map(int,input().split()))
i=0
bl = True
while(bl):
    for j in range(5):
        if list1[i][j]==1:
            print(abs(2-i)+abs(2-j))
            bl =False
    i+=1
    
    