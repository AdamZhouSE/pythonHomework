nk=input().split(' ')
n=int(nk[0])
k=int(nk[1])
sqs=[]
for i in range(n):
    sq=input().split(' ')
    sq=list(map(int,sq))
    sqs.append(sq)
area=[]
for i in range(n):
    for j in range(i+1,n):
        sq_1=sqs[i]
        sq_2=sqs[j]
        if sq_1[0]+k<=sq_2[0] or sq_2[0]+k<=sq_1[0] or sq_1[1]+k<=sq_2[1] or sq_2[1]+k<=sq_1[1]:
            continue
        if sq_1[0]<=sq_2[0]:
            row=sq_1[0]+k-sq_2[0]
        else:row=sq_2[0]+k-sq_1[0]
        if sq_1[1]<=sq_2[1]:
            col=sq_1[1]+k-sq_2[1]
        else:col=sq_2[1]+k-sq_1[1]
        area.append(row*col)
if len(area)==0:
    print(0)
elif len(area)==1:
    print(area[0])
else:
    print(-1)