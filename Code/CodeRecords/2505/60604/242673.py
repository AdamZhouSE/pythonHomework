a=input().split(',')
#print(a)
for i in range(1,len(a)):
    for j in range(i):
        if a[j]==a[i]:
            print(a[j])
            break