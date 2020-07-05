a=input()
flag=1
for i in range(len(a)):
    for j in range(i):
        if a[j]<a[i]:
            continue
        else:
            flag=0
            break
print(flag)
        