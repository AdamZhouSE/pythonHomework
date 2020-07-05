def go(l):
    l = list(l)
    if not l:
        return True
    else:
        cst = l.pop()
        i = 0
        left = []
        right = []
        while i < len(l):
            if l[i]<cst:
                left.append(l[i])
                i+=1
            else:
                break
        while i<len(l):
            if l[i]>cst:
                right.append(l[i])
                i+=1
            else:
                break
        if i< len(l):
            return False
        else:
            return go(left) and go(right)


input()
try:
    li = [int(i) for i in input().split()]
    print(str(go(li)).lower())
except:
    print('true')