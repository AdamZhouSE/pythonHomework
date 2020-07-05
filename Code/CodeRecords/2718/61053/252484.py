def process_set(str_lst,index):
    lst = []
    for i in index:
        lst.append(str_lst[i])
    lst = sorted(lst)
    count = 0
    for i in index:
        str_lst[i] = lst[count]
        count = count + 1
    #print(str_lst)
    return str_lst



string = input()
str = list(string)

pairs = eval(input())
list = []
for i in range(0,len(pairs)):
    a = pairs[i][0]
    b = pairs[i][1]
    exist = False
    for j in range(0,len(list)):
        if (a in list[j]) or (b in list[j]):
            list[j].add(a)
            list[j].add(b)
            exist = True
            break
    if not exist:
        new_set = set()
        new_set.add(a)
        new_set.add(b)
        list.append(new_set)
for i in range(0,len(list)):
    str = process_set(str,list[i])
ans = "".join(str)
print(ans)