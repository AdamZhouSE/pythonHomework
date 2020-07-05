row=eval(input())
count=0
seats={x:i for (i,x) in enumerate(row)}
for i in range(0,len(row),2):
    x=row[i]
    if x%2==0:
        y=x+1
    else:
        y=x-1
    j=seats[y]
                        
    if abs(i-j) > 1: 
        row[i+1], row[j] = row[j], row[i+1]
        seats[row[i+1]], seats[row[j]] = i+1, j              
        count += 1
print(count)