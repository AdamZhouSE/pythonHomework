def findRoutines(beginW,endW,lst) ->int:
    if endW not in lst:
        return 0
    pre=set()
    pre.add(beginW)
    if beginW in lst:
        remain = set(lst.remove(beginW))
    else:
        remain = set(lst)#if beginW in lst, remove it
    visited=pre
    cnt=0
    while remain and endW not in pre:#还没找空并且没找到endW
        current_level=set()
        for i in pre:
            for j in remain:
                diff=set(i).difference(set(j))#different alphas in words
                if (len(diff)==1):
                    current_level.add(j)
        if current_level:#z这一层有符合条件的变词
            cnt+=1
            visited=visited.union(current_level)
            pre=current_level
            remain=remain.difference(current_level)
    return cnt+1#花了cnt steps 单词长度是加一之后的结果

if __name__=="__main__":
    beginW = input()
    endW = input()
    lst = eval(input())  # 使用集合的set1.difference(set2)方法 列表和字符串都可以使用
    res=findRoutines(beginW,endW,lst)
    print(res)
