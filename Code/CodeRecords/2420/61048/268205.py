def numop5():
    num=int(input())
    res=[]
    for i in range(1,num):
        if (hasnozero(i) and hasnozero(num-i)):
            res.append(i)
            res.append(num-i)
            break
    print(res)
    return

def hasnozero(num):
    string=str(num)
    haszero=True
    for word in string:
        if word=='0':
            haszero=False
            break
    return haszero

numop5()