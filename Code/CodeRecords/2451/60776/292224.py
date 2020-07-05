a=input()
b=a.split(',')
for i in range(0,len(b)):
    b[i]=int(b[i])
target=int(input())
b.append(target)
b.sort()
for i in range(0,len(b)):
    if b[i]==target:
        print(i)
        break