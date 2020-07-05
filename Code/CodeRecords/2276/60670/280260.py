r=int(input())
c=int(input())
r0=int(input())
c0=int(input())
n=r*c-1
leng=0
times=0
loc=0
queue=[]
queue.append([r0,c0])
while n>0:
    if times==0:
        leng+=1
    if loc==0:
        c0+=leng
    elif loc==1:
        r0+=leng
    elif loc==2:
        c0-=leng
    elif loc==3:
        r0-=leng
    loc=(loc+1)%4
    times=(times+1)%2
    #print(r0,c0)
    if (r0>=0)and(r0<r)and(c0>=0)and(c0<c):
        n-=1
        queue.append([r0,c0])
print(queue)