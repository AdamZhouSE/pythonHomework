def test17():
    n=int(input())
    x=input().split(" ")
    a=[]
    for item in x:
        a.append(int(item))
    b=set(a.sort())
    return b[1]-b[0]
print(test17())