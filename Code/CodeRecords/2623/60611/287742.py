l=list(map(int,input().split(",")))
number=int(input())
l=sorted(l)
l=l[::-1]
print(l[number-1])