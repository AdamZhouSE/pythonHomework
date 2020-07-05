temp=input().split()
c=int(temp[0])
n=int(temp[1])
sta=[[0]*10 for i in range(10)]

for i in range(n):
    pos=[int(x) for x in input().split()]
    x=pos[0]
    y=pos[1]
    sta[x-1][y-1]+=1
    
for i in range(10):
    for j in range(0,10-i):
        for k in range(0,10-i):
            sum=0
            for m in range(j,j+i):
                for n in range(k,k+i):
                    sum+=sta[m][n]
            if(sum>=c):
                print(i)
                break
        if(sum>=c):
            break
    if(sum>=c):
            break

    
