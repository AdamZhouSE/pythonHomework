# def isCover(s1,s2):
#     if len(s1)>len(s2) and s2[0] in s1:
#         return True
#     else: return False
# def isAnother(s1,s2):
#     for i in s2:
#         if
s1=input()
s2=input()
l=s2[2:len(s2)-2].split("],[")
#print(l)

step=[]
for i in range(len(s1)):
    s=[]
    step.append(s)

for i in range(len(l)):
    item=l[i].split(",")
    n1=int(item[0])
    n2=int(item[1])
    step[n1].append(n2)
    for j in range(len(step)):
        if n1 in step[j]:
            step[j].append(n2)
    step[n2].append(n1)
    for j in range(len(step)):
        if n2 in step[j]:
            step[j].append(n1)
for i in range(len(step)):
    c=set(step[i])
    step[i]=list(c)
#print(step)
# for i in range(len(l)):
#     if isCover(step[i],step[i+1]):
#         t=step[i+1]
#         step[i+1]=step[i]
#         step[i]=t
adj=list(s1)
#print(adj)
for i in step:
    i.sort()
    str=[]
    for j in i:
        str.append(adj[j])
    str.sort()
    for k in range(len(i)):
        adj[i[k]]=str[k]
result=""
for i in adj:
    result=result+i
print(result)