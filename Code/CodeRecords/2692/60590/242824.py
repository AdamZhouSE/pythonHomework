weights=(input()[1:-1]).split(',')
weights=[int(x) for x in weights]
d=int(input())
average=int(sum(weights)/d)
for i in range(average,average**2):
    count=0;temp=0
    found=True
    for j in range(len(weights)):
        if temp<=i and temp+weights[j]>i:
            count+=1
            temp=weights[j]
        elif temp>i:
            found=False
            break
        else:
            temp+=weights[j]
    if count<=d-1 and found:
        print(i)
        break