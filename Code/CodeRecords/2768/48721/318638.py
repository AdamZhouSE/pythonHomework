t = int(input())
for i in range(t):
    inp = input().split(' ')
    a = int(inp[0])
    b = int(inp[1])
    m = int(inp[2])
    count = 0
    temp = []
    #print("m: ",m)
    for j in range(1,100,1):
        temp.append(j * m)
    #print(temp)
    #print(count)
    for k in temp:
        if(k>=a and k<=b):
            count =count +1
    print(count)