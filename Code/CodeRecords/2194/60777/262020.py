t=int(input())

def prime(x):
    for i in range(2,x):
        if(x%i==0):
            return False
    return True

for i in range(t):
    temp=[int(x) for x in input().split()]
    eve=[]
    for j in range(temp[0],temp[1]+1):
        if(prime(j) and j!=1):
            eve.append(str(j))
    print(' '.join(eve))
