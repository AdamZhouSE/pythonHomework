T = int(input())
source = []
for x in range(0,T):
    source.append(int(input()))
for x in range(0,T):
    n = source[x]
    for b in range(1,100):
        if n+2>2**b and n+2 <= (2**(b+1)):
            break
    num = n+1-2**b
    result=''
    #对num进行带余除法
    for z in range(0,b):
        if num%2 == 1:
            result="7"+result
        elif num%2 == 0:
            result="4"+result
        num=num//2
    print(result)