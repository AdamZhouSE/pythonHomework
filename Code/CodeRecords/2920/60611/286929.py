l=[]
l.append(list(map(int,input().split(" "))))
l.append(list(map(int,input().split(" "))))
sub=[]
for i in range(1,l[0][0]):
    sub.append(l[1][i]-l[1][i-1])
sub=sorted(sub)
result=sum(sub[0:len(sub)-l[0][1]+1])
print(result)