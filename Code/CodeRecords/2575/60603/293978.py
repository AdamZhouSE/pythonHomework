def maxDepthAfterSplit(seq):
        d = 0
        dlst = []
        for i in seq:
            if i == '(':
                dlst.append(d)
                d += 1
            else:
                d -= 1
                dlst.append(d)
        return [i%2 for i in dlst]
    
str1=input()
print(maxDepthAfterSplit(str1))