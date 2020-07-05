def test10():
    n=int(input())
    left=input().split(" ")
    x=input().split(" ")
    bottle=[]
    suml=0
    for item in left:
        suml=suml+int(item)
    for item in x:
        bottle.append(int(item))
    bottle.sort()
    cap=bottle[n-1]+bottle[n-2]
    if(cap>suml):
        return "YES"
    else:
        return "NO"
print(test10())
