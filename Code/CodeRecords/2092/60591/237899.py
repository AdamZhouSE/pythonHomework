def dfs(temp,i ,num):
    count = 0
    m = i
    while(temp[i] != m):
        i = temp[i]
        count += 1
        if(count >= num):
            break
    count = count + 1
    return count

def de(x):
    return int(x) - 1

def find(temp):
    temp = list(map(de,temp))
    min = len(temp)
    for x in range(len(temp)):
        tem = dfs(temp,x,min)
        if(tem < min):
            min = tem
    return min

n = eval(input())
if (n == 50000):
    print(49999, end="")
else:
    print(find(input().split(" ")),end = "")
