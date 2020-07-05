temp=[int(x) for x in input().split(' ')]
n=temp[0]
m=temp[1]
out=[0]*n
for i in range(m):
    ticket=[int(x) for x in input().split(' ')]
    for j in range(n):
        win=max(ticket)
        ind=ticket.index(win)
        out[ind]+=1
        
last=max(out)
print(out.index(last)+1)