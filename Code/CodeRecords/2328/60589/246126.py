a=list(map(int,input().split(',')))
ans=[]


def doIt():
    can=True
    if 2 in a:
        ans.append(2)
        a.remove(2)
        can=False
    elif 1 in a:
        ans.append(1)
        a.remove(1)
    elif 0 in a:
        ans.append(0)
        a.remove(0)
    else:
        return ''

    if 9 in a and can:
        ans.append(9)
        a.remove(9)
    elif 8 in a and can:
        ans.append(8)
        a.remove(8)
    elif 7 in a and can:
        ans.append(7)
        a.remove(7)
    elif 6 in a and can:
        ans.append(6)
        a.remove(6)
    elif 5 in a and can:
        ans.append(5)
        a.remove(5)
    elif 4 in a and can:
        ans.append(4)
        a.remove(4)
    elif 3 in a:
        ans.append(3)
        a.remove(3)
    elif 2 in a:
        ans.append(2)
        a.remove(2)
    elif 1 in a:
        ans.append(1)
        a.remove(1)
    elif 0 in a:
        ans.append(0)
        a.remove(0)
    else:
        return ''

    if 5 in a:
        ans.append(5)
        a.remove(5)
    elif 4 in a:
        ans.append(4)
        a.remove(4)
    elif 3 in a:
        ans.append(3)
        a.remove(3)
    elif 2 in a:
        ans.append(2)
        a.remove(2)
    elif 1 in a:
        ans.append(1)
        a.remove(1)
    elif 0 in a:
        ans.append(0)
        a.remove(0)
    else:
        return ''

    if 9 in a:
        ans.append(9)
        a.remove(9)
    elif 8 in a:
        ans.append(8)
        a.remove(8)
    elif 7 in a:
        ans.append(7)
        a.remove(7)
    elif 6 in a:
        ans.append(6)
        a.remove(6)
    elif 5 in a:
        ans.append(5)
        a.remove(5)
    elif 4 in a:
        ans.append(4)
        a.remove(4)
    elif 3 in a:
        ans.append(3)
        a.remove(3)
    elif 2 in a:
        ans.append(2)
        a.remove(2)
    elif 1 in a:
        ans.append(1)
        a.remove(1)
    elif 0 in a:
        ans.append(0)
        a.remove(0)
    return str(ans[0])+str(ans[1])+':'+str(ans[2])+str(ans[3])


print(doIt())