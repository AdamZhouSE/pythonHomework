def shift(string):
    return string[-1] + string[:-1]

input()
temp = list(map(int,input().split(" ")))
tem = temp.copy()
tem.sort()
tem = list(map(str,tem))
result = "".join(tem)
n = len(temp)
temp = list(map(str,temp))
res = "".join(temp)
situation = True
while(n != 0):
    n = n - 1
    if(res==result):
        situation = False
        print(len(temp) - n - 1)
        break
    res = shift(res)
if(situation):
    print(-1)


