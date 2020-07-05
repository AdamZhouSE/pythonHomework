aaa=input()
l=aaa.split(",")
l= list(map(int, l))
gap=int(input())

res=0

for i in range(len(l)):
    currLen=1
    for j in range(i+1, len(l)):
        if l[i]+currLen*gap==l[j]:
            currLen+=1
    res=max(res, currLen)

print(res)