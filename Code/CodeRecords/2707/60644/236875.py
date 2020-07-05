a=input()
a=a[1:-1].split(',')
for i in range(0,len(a)):
    a[i]=int(a[i])
    a[i]=int(a[i]/2)
res=0
for i in range(0,len(a),2):
    if a[i]!=a[i+1]:
        for j in range(0,len(a)):
            if a[j]==a[i] and j!=i:
                temp=a[j]
                a[j]=a[i+1]
                a[i+1]=temp
                res=res+1              
print(res)