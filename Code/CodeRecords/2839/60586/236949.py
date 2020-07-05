def test11():
    n=int(input())
    name=[]
    result="NO"
    for i in range(n):
        name.append(input())
    for i in range(1,n):
        str = "NO"
        for j in range(0,i):
            if name[i]==name[j]:
                str="YES"
        result=result+'\n'+str
    return result
print(test11())

