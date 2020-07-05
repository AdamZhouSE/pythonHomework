a=list(map(int,input().split(',')))
for i in range(len(a)):
    if abs(a[i]-i)>1:
        print(False)
        break
else:
    print(True)