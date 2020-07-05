l=eval(input())
n=int(input())
pair=sorted([(l[i],l[j]) for i in range(len(l)) for j in range(i+1,len(l))]\
            ,key=lambda x:abs(x[1]-x[0]))
print((lambda x:abs(x[1]-x[0]))(pair[n-1]))