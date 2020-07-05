aaa=input()
aaa=aaa[1:len(aaa)-1]
l=aaa.split(",")
l= list(map(int, l))
target=int(input())
if target in l:
    for i in range(len(l)):
        if l[i]==target:
            print(i)
else:
    print(-1)