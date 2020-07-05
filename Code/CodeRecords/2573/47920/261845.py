import math
'''def odd(n):
    result = 0
    for i in range(int(n/2)):
        print("oushu {}".format(int(n/2)))
        if(i == 1):
            result = 2
        else:
            print(odd(n-2),3)
            result = math.pow(odd(n-2),3)
    return result'''
inp = int(input())
for i in range(inp):
    i = int(input())
    #print(i)    
    mu = 1    
    for k in range(0,i-1):
        mu = mu*2    
    print(mu)