t = int(input())
for i in range(t):
    temp = []
    inp = input().split(' ')
    n = int(inp[0])
    k = int(inp[1])
    li = input().split(' ')
    for j in li:
        temp.append(int(j))
    '''print('n: ',n)
    print("k: ",k)
    print(temp)'''
    count = 0
    for t in temp:
        if(t<=k):
            count = count +1
    print(count)