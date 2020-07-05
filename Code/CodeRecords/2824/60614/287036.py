init=[int(x) for x in input().split()]
length=init[0]
maximum=init[1]
number=init[2]
prisoner=[int(x) for x in input().split()]
i=0
count=0
while i<=length-number:
    judge=True
    for j in range(i,i+number):
        if prisoner[j]>maximum:
            i=j+1
            judge=False
            break
    if judge:
        count+=1
        i+=1
print(count)