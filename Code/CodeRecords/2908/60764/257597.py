n=int(input())
type=[]
for i in range(n):
    l=list(input())
    l.sort()
    if " " in l:
        l.remove(" ")
    if l not in type:
        type.append(l)
print(len(type),end="")