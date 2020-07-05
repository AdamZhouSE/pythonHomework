    n=int(input())
    x=input().split(" ")
    a=[]
    for item in x:
        a.append(int(item))
    a.sort()
    b=[]
    for item in set(a):
        b.append(item)
    return b[1]-b[0]
print(test17())