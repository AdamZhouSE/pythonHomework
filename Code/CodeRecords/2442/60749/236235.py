a=input()
a=sorted(a)
if len(a)<2:
    print("0")
else:
    max=0
    for x in range(1,len(a)):
        if a[x]-a[x-1]>max:
            max=a[x]-a[x-1]
    print(max)
    