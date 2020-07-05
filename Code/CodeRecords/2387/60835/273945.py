n = input().split(' ')
tem = input().split(' ')
group = []
for x in tem:
    group.append(int(x))
def sort(mark,group,start,end):
    new = []
    for x in range(start):
        new.append(group[x])
    tem = []
    for x in range(start,end + 1):
        tem.append(group[x])
    if mark == 1:
        tem.sort(reverse = True)
    else:
        tem.sort()
    new.extend(tem)
    for x in range(end + 1,len(group)):
        new.append(group[x])
    return new
for x in range(int(n[1])):
    tem = input().split(' ')
    group = sort(int(tem[0]),group,int(tem[1]) - 1,int(tem[2]) - 1)
print(group[int(input()) - 1])