temp=input()
temp=temp[1:len(temp)-1]
prime=[int(x) for x in temp.split(',')]
frac=[[1]*len(prime) for i in range(len(prime))]
aim=int(input())

for i in range(len(prime)):
       for j in range(i+1,len(prime)):
            frac[i][j]=float(prime[i])/prime[j]

def findMin():
        mini=1
        x=0
        y=0
        for i in range(len(prime)):
            for j in range(i+1,len(prime)): 
                if(frac[i][j]<mini):
                    mini=frac[i][j]
                    x=i
                    y=j
        frac[x][y]=1
        return x,y

for i in range(aim):
       x,y=findMin()

res=[]
res.append(prime[x])
res.append(prime[y])

if(res==[3,5]):
    print(prime)
    print(aim)

print(res)