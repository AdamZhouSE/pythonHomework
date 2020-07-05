inp=list(map(int,input().split(',')))
list=[[] for i in range(4)]
for i in range(4):
    list[i].append(inp[2*i])
    list[i].append(inp[2*i+1])
s1=(list[1][0]-list[0][0])*(list[1][1]-list[0][1])
s2=(list[3][0]-list[2][0])*(list[3][1]-list[2][1])
soverlap=abs(list[3][1]-list[1][1])*abs(list[1][0]-list[2][0])
result=s1+s2-soverlap
print(result)
