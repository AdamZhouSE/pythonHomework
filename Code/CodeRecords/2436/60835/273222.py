group = eval(input())
new = eval(input())
start = 0
end = 0
#print(new,group)
for i in group:
    if new[0] <= i[1] and new[0] >= i[0]:
        new[0] = i[0]
        start = group.index(i)
        end = group.index(i)
        #print(new)
    if new[1] >= i[0] and new[1] <= i[1]:
        new[1] = i[1]
        end = group.index(i)
#print(start,end)
length = len(group)
while len(group) > (length - (end - start + 1)):
    del group[start]
    #print(len(group))
group.insert(start,new)
print(group)