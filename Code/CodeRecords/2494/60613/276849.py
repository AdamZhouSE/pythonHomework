J=eval(input())
result=0

for i  in range(len(J)-1):
    for  j in range(i+1,len(J)):
        if J[i]>2*J[j]:
            result+=1
            
print(result)
            