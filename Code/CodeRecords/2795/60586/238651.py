def test17():
    n=int(input())
    x=input().split(" ")
    a=[]
    for item in x:
        a.append(int(item))
    a.sort()
    b=[]
    add=0
    for item in set(a):
        add =add+item
        b.append(item)
    ave=add/len(set(a))
    if len(set(a))>3:
        return -1
    return b[1]-b[0]
print(test17())