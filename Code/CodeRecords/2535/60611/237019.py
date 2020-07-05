source = str(input())
assist = list(map(int, source[1:-1].split(",")))
count=0
for i in range(len(assist)):
    mid=sorted(assist[0:i+1])
    if mid[-1]==i:
        count+=1
print(count)