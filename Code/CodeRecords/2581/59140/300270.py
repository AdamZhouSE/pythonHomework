def manhaton_distance(s,target):
    s=s.split(",")
    return abs(int(s[0])-int(target[0]))+abs(int(s[1])-int(target[1]))


ghostnum=int(input())
ghost=[]
for _ in range(ghostnum):ghost.append(input())
target=input().split(",")
mine=manhaton_distance("0,0",target)
flag=True
for i in ghost:
    if manhaton_distance(i,target)<=mine:flag=False
print(flag)