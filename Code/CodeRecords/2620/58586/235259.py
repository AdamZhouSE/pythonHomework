lines=int(input())
for i in range(lines):
    sum=0
    line=int(input())
    for j in range(1,line+1):
        sum+=pow(j,5)
    print(sum)
    i+1