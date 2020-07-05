l=eval(input())
for i in range(len(l)-1,-1,-1):
    temp=l[i][1]
    sum1=1
    index=0
    for j in range(len(l)):
        if l[i][1]==l[j][1]:
            sum1+=1
            index=j
    if (sum1>=2):
        print(l[j])
        break;