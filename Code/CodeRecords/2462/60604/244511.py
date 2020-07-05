a=input().split(",")
for i in range(len(a)):
    if i==0:
        if a[i]>a[1]:
            print(0)
            break
    elif i==len(a)-1:
        if a[i]>a[i-1]:
            print(i)
            break
    else:
        if a[i]>a[i-1] and a[i]>a[i+1]:
            print(i)
            break