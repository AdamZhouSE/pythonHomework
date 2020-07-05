num = int(input())
x=input().split(' ')
x=list(map(int,x))
magic=[]
for i in range(0,num-1):
    con=[]
    temp=i
    con.append(x[i])
    for j in range(i+1,num):
        if x[j]>x[temp] and x[j]<=2*x[temp]:
            con.append(x[j])
        else :
            break
        temp+=1
    magic.append(con)
maxLen=0
for i in magic:
    if len(i)>maxLen:
        maxLen=len(i)
if len(x)==1:
    maxLen=1
print(maxLen)