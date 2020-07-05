
def turn(a):
    temp=list(a)
    cons=[]
    cons.append(int(temp[0]))
    for i in range(len(temp)-1):
        cons.append(int(cons[i])^ int(temp[i+1]))
    return ''.join([str(x) for x in cons])
        
n=int(input())
for i in range(n):
    bina=bin(int(input()))
    print(int(turn(bina[2:]),2))