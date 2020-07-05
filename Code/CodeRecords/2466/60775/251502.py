def tri(e1,e2,e3):
    '''给三条边长度，返回是否能组成三角形'''
    if e1+e2>e3 and e1+e3>e2 and e2+e3>e1:
        return 1
    else:
        return 0

def cal(lis):
    result = 0
    for i in range(len(lis)-2):
        for j in range(i+1,len(lis)-1):
            for k in range(j+1,len(lis)):
                result += tri(lis[i],lis[j],lis[k])
    return result

t = int(input())
test = []
result = []
for i in range(t):
    length = int(input())
    str = input().split(' ')
    test.append([int(i) for i in str])
    result.append(cal(test[-1]))

for i in result:
    print(i)