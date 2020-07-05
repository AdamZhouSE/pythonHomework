a=[int(x) for x in input().split(",")]
a.sort(reverse=True)
for i in range(len(a)-2):
    if a[i]<a[i+1]+a[i+2]:
        print(a[i]+a[i+1]+a[i+2])
        break
    elif(i==len(a)-3):
        print(0)