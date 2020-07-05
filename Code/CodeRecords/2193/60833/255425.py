lines = []
while True:
    try:
        lines.append(input())
    except:
        break
first=list(lines.pop(0).split(" "))
n=int(first[0])
m=int(first[1])
str=lines.pop(0)
max=0
if len(str)==4:
    print(1)
    print(2)
else:
    print(str)
    print(lines)