l=input().split(",")
n=int(input())
if n>int(l[-1]):
    print(len(l))
for i in range(len(l)):
    if n==int(l[i]):
        print(i)
        break
    elif n>int(l[i]):
        pass
    else:
        print(i)
        break