start=[1]
for line in range(1,100):
    start.append(start[line-1]+2*line)
for n in range(int(input())):
    line=int(input())
    rs=0
    for i in range(start[line-1],start[line-1]+2*line):
        rs+=i
    print(rs)