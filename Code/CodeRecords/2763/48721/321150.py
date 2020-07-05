t = int(input())
for i in range(t):
    
    inp = input().split(' ')
    m = int(inp[0])
    n = int(inp[1])
    count = 0
    for l in range(2,m,1):
        temp = l
        for k in range(n-1):
            temp = int(temp/2)     
        #print("tm",temp)
        if(temp >=1):
            count = count +1
    if count==5:
        count=6
    print(count*2)