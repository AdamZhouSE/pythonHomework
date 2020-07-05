lists=list(input().split(","))
x=str(input())
start=-1
end=-1

for i in range(0,len(lists)):
    if x==lists[i]:
        if start==-1:
            start=i
        if start!=-1:
            end=i

print("["+str(start)+", "+str(end)+"]")