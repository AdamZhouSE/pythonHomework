n=int(input())
myarray=[[0]*2]*n
for i in range(n):
    s=input()
    myarray[i]=list(map(int,s.split(",")))
k1=(myarray[0][1]-myarray[1][1])/(myarray[0][0]-myarray[1][0])
for i in range(1,n-1):
    k=(myarray[i][1]-myarray[i+1][1])/(myarray[i][0]-myarray[i+1][0])
    if(k1!=k):
        print(True)
        break
else:
    print(False)
