t = int(input())
for k in range(t):
    n = int(input())
    a = [int(i) for i  in input().split(" ")]
    frequent = {}
    for x in a:
        if frequent.get(x) == None:
            frequent[x] = 1
        else:
            frequent[x] +=1
    frequent1 = sorted(frequent.items(),key=lambda x:(-x[1],x[0]))
    for i in range(len(frequent1)):
        key = int(str(frequent1[i]).replace("(","").replace(",","").replace(")","").split(" ")[0])
        times = int(str(frequent1[i]).replace("(","").replace(",","").replace(")","").split(" ")[1])
        for j in range(times):
            if i == len(frequent1)-1 and j == times-1:
                print(key,end=" ")
                print()
            else:
                print(key,end=" ")
