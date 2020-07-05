def test17():
    n=int(input())
    x=input().split(" ")
    a=[]
    for item in x:
        a.append(int(item))
    a.sort()
    b=[]
    ave=[]
    add=0
    for item in set(a):
        add =add+item
        b.append(item)
    ave.append(add/len(set(a)))
    if len(set(a))>3:
        print(x)
        return -1
    if set(ave).issubset(set(a)):
        return b[1]-b[0]
    return -1
print(test17())
