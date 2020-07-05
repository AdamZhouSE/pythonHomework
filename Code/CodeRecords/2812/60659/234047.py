n=int(input())
l=input().split(' ')
l=list(set(l))
length=len(l)
for x in l:
    if x=="0":
        length-=1
print(length)