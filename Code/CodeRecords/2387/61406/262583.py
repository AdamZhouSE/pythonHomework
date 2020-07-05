one=input().split(' ')
n = int(one[0])
m = int(one[1])
init = input().split(' ')
init = [int(x) for x in init]
for a in range(0,m):
    operation = input().split(' ')
    start = int(operation[1])-1
    end = int(operation[2])-1
    if operation[0]=='0':#升序
        init = init[0:start]+sorted(init[start:end+1])+init[end+1:]
    elif operation[0]=='1':#降序
        init = init[0:start]+sorted(init[start:end+1], reverse=True)+init[end+1:]
target = int(input())-1
print(init[target])