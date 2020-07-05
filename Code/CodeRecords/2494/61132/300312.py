l=eval(input())
ans=[1 if l[i]>l[j]*2 else 0 for i in range(len(l)) for j in range(i+1,len(l))]
print(sum(ans))