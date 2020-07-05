def changeItem(index:int):
    if int(strs[index])==lists[index]:
        if index==len(strs)-1: 
            return strs
        t = changeItem(index+1)
        return t
    else:
        temp = lists[index]
        locate = strs.rfind(str(temp))
        k = list(strs)
        k[locate] = strs[index]
        strs[index] = temp
        return ''.join(k)
        
strs = input()
#print(strs)
lists = [int(i) for i in list(strs)]
lists.sort()
lists.reverse()
ans = changeItem(0)
print(ans)