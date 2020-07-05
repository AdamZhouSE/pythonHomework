# 判断str,list,tuple,dict是否为空：若空则 not+名字 为True
str = list(input())
l = [set(i) for i in eval(input())]
while True:
    can_break = True
    l_after = [l[0]]
    for i in range(1,len(l)):
        have_intersection = False
        for j in range(len(l_after)):
            if not l_after[j].isdisjoint(l[i]):#有交集
                have_intersection = True
                can_break = False
                l_after[j]=l_after[j].union(l[i])
                break
        if not have_intersection:#无交集
            l_after.append(l[i])
    l = l_after
    if can_break==True:
        break
# 集合s可以通过list(s)转化为列表(此题不用)
for s in l_after:
    chr_list = []
    index_list = list(s)
    for i in s:
        chr_list.append(str[i])# i直接就是int型
    chr_list.sort()
    index_list.sort()
    for i in range(len(index_list)):
        str[index_list[i]] = chr_list[i]
res = ''.join(str)
print(res)