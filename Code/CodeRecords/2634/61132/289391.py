l=sorted(eval(input()))
k=int(input())
new = [[l[i],l[j]] for i in range(len(l)) for j in range(i+1,len(l))]
new=sorted(new,key=lambda x:x[0]/x[1])
print(new[k-1])