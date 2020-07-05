l=eval(input())
k=int(input())
l=sorted(l,key=lambda x:x[0]*x[0]+x[1]*x[1])
print([l[i] for i in range(k)])