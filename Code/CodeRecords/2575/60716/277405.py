def find_Depth(i:int,loc:int):
    while loc<len(strs):
        if strs[loc]=='(':
            lists.append(i)
            loc = find_Depth(i+1,loc+1)
        elif strs[loc]==')':
            lists.append(i-1)
            return loc
strs = input()
lists = list()
find_Depth(0,0)
print(lists)