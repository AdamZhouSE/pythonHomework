row=eval(input())
count=0
for i in range(0,len(row),2):
    if int(row[i]/2)==row[i]/2:
        if row[i+1]==row[i]+1:
            break
        else:
            temp=row[i+1]
            row[i + 1] = row[i] + 1
            for j in range(i+2,len(row)):
                if row[j]==row[i] + 1:
                    row[j]=temp
            count+=1
    else:
        if row[i+1]==row[i]-1:
            break
        else:
            temp=row[i+1]
            row[i + 1] = row[i] - 1
            for j in range(i+2,len(row)):
                if row[j]==row[i] - 1:
                    row[j]=temp
            count+=1
print(count)