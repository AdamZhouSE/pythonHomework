x=str(input())
y=[int(i) for i in x[1:len(x)-1].split(",")]
count=0
for i in range(len(y)-1):
    for j in range(i+1,len(y)):
        if y[i]>2*y[j]:
            count += 1
print(count)