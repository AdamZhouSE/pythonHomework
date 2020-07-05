import itertools
def dist(p1,p2):
    return (p2[1]-p1[1])**2+(p2[0]-p1[0])**2
def check(list0):
    return dist(list0[0],list0[1])==dist(list0[1],list0[2]) and dist(list0[1],list0[2])==dist(list0[2],list0[3]) and dist(list0[2],list0[3])==dist(list0[3],list0[0])and dist(list0[3],list0[0])==dist(list0[0],list0[1])and dist(list0[0],list0[2])==dist(list0[1],list0[3])
list1=[]
for i in range(0,4):
    line=input().split(",")
    line=list(map(int,line))
    list1.append(line)
list2=list(itertools.permutations(list1))
j=False
for list0 in list2:
    if(check(list0)):
        j=True
        break
print(j)
