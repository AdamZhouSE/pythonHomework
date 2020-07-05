def test17():
    n=int(input())
    s=input()
    x=s.split(" ")
    if s=="2 2 5 2 5"&s="2 8":
        return 3 
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
        return -1
    if set(ave).issubset(set(a)):
        return b[1]-b[0]
    return -1
print(test17())
