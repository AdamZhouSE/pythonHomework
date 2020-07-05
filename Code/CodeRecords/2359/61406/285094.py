def triples(x,y,z):
    if x+y==z:
        return True
    elif x+z==y:
        return True
    elif y+z==x:
        return True
    else:
        return False


T = int(input())
for a in range(0,T):
    N = int(input())
    source = input().split(' ')
    count = 0
    for i in range(0,N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if triples(int(source[i]),int(source[j]),int(source[k])):
                    count += 1
    if count==0:
        print(-1)
    else:
        print(count)