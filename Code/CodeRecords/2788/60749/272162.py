n=int(input())
boys=list(map(int,input().split(" ")))
m=int(input())
girls=list(map(int,input().split(" ")))
girls=sorted(girls)
count=0
for h in girls:
    for m in boys:
        if abs(h-m)<=1:
            count+=1
            boys.remove(m)
            break
print(count)