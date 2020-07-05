n=int(input())
num=0
def s(x,y):
    su=0
    for i in range(x,y+1):
        su+=i
    return su
for i in range(1,n+1):
    for j in range(i,n+1):
        if(s(i,j)==n):
            num+=1
print(num)