l = eval(input())
l.sort()
for i in range(len(l)-1,-1,-1):
    if i-2>=0:
        if l[i]<l[i-1]+l[i-2]:
            print(l[i]+l[i-1]+l[i-2])
            break
    