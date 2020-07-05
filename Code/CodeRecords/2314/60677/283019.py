times=int(input())
answer=[]
line=input().split()
answer.append(line[0])
answer.append(line[2])
answer.insert(0,line[1])
for i in range(times-1):
    line=input().split()
    index=answer.index(line[0])
    if line[2]!="0":
        answer.insert(index+1,line[2])
    if line[1]!="0":
        answer.insert(index,line[1])
print(" ".join(answer),end=" ")