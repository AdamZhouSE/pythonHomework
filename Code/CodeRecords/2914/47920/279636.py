temp = []
n = int(input())
for i in range(n):
    length = int(input())
    inp1 = input().split(' ')
    inp2 = input().split(' ')
    if(length==0):
        if(inp1[0] > inp2[0]):
            print("NO")
        else:
            print("YES")
    else:
        for i in range(length):
            temp.append(int(inp2[i])-int(inp1[i]))
        temp.sort(key=None, reverse=True)
        #print(temp)
        count=0
        for i in temp:
            if(i == 0):
                count+=1
        co = temp[0]
        flag = True
        if(count==length):
            print("YES")
        else:
            for j in range(length-count):
                if(co != temp[i]):
                    flag = False
            if(flag):
                print("YES")
            else:
                print("NO")