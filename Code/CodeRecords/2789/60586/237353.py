def test14():
    k=int(input())
    result=""
    for i in range(k-1):
        n=int(input())
        x=input().split(" ")
        d=[]
        for item in x:
            d.append(int(item))
        d.sort(True)
        line=1
        for i in range(1,n):
            if(d[i-1]>=d[i]):
                line=line+1
            if line==d[i]:
                result=result+"\n"+line
        return result[0:len(result)-1]
print(test14())