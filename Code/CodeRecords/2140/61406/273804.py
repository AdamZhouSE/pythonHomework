T = int(input())
for a in range(0,T):
    N = int(input())
    result = []
    for x in range(0,N):
        result.append(0)
    pos = 0
    for i in range(1,N+1):
        count = i
        while count!=0:
            if result[pos]==0:
                count = count-1
            pos = (pos+1)%N
        while result[pos]!=0:
            pos = (pos+1)%N
        result[pos]=i
    string =""
    for y in result:
        string = string+str(y)+" "
    print(string.rstrip(' '))



