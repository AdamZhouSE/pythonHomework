t = int(input())
for i in range(t):
    temp = []
    n = int(input())
    li = input().split(' ')
    for j in li:
        temp.append(int(j))
    mx = max(temp)
    mn = min(temp)
    #print(mx)
    #print(mn)
    if(mx%mn == 0):
        print(mx)
    else:
        print(mx * mn)