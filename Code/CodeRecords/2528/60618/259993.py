line=eval(input())
for i in range(1,len(line)):
    for j in range(0,len(line)-i):
        if line[j]>line[j+1]:
            line[j],line[j+1]=line[j+1],line[j]
print(line)