n=int(input())
for I in range(n):
    s=list(input())
    tmp=[]
    #print(s)
    res=0
    for i in range(0,len(s)):
        if s[i].isdigit():
            tmp.append(s[i])
       #     print(tmp)
        else:
            x=tmp.pop()
            x="x="+tmp.pop()+s[i]+x
            exec(x)
            tmp.append(str(x))
          #  print(tmp)
    print(tmp[0])
    