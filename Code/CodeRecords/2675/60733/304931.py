for _ in range(int(input())):
    a=str(input())
    res=""
    for i in a:
        if i=='6':
            res+='9'
        else:
            res+=i
    
    print(int(res)-int(a))      