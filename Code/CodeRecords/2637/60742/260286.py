a = eval(input())
for i in range(1,len(a)):
    if a[i-1]>=a[i]:
        print(i-1)
        break