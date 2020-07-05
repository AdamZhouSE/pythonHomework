t=eval(input())
for _ in range(t):
    n=bin(eval(input())).replace('0b','')
    res=n[0]
    for i in range(1,len(n)):
        if res[-1]==n[i]:
            res+='0'
        else:
            res+='1'
    print(int(res,2))
        
    