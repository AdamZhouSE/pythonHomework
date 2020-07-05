info=input()
a=[int(y) for y in info[1:-1]]
k=int(input())
b=[]
for i in range(len(a)-1):
    for j in range(i+1,len(a)):        
        b.append(abs(a[j]-a[i]))
print(b)        