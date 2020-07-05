a=[]
for i in range(101):
    count=0
    while i>=5:
        if i%5==0:
            i=i/5
            count=count+1
    a.append(count)   
print(a)