T=int(input())

def happyNumber(x):
    string=str(x)
    count=0
    for a in string:
        count=count+int(a)*int(a)
    return count

for i in range(0,T):
    start=int(input())+1
    a=True
    while a:
        posi=start
        path=[]
        while True:
            if posi==1:
                print(start)
                a=False
                break
            if posi in path:
                break
            path.append(posi)
            posi=happyNumber(posi)
        start=start+1
