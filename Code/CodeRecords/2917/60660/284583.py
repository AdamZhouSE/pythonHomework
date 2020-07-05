n=int(input())
#l=eval('['+input().replace(' ',',')+']')
l=[]
for i in range(n):
    l.append(eval('('+input().replace(' ',',')+')'))
sum=0
for i in range(n):
    for j in range(i+1,n):
        if l[j][0]==l[i][0] or l[j][1]==l[i][1]:
            sum+=1
print(sum)