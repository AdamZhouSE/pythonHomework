num=int(input())
arr=[]

def cal(x):
    cons='0'+bin(x)[2:]
    cons=list(cons)
    cons.reverse()

    for i in range(len(cons)-1):
        if(i%2==0):
            temp=cons[i]
            cons[i]=cons[i+1]
            cons[i+1]=temp
    cons.reverse()
    return  ''.join(cons)
for i in range(num):
    a=int(input())
    print(int(cal(a),2))