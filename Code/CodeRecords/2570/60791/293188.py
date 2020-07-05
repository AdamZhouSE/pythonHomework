n = int(input())
env = []
x = n
while x > 0:
    x-=1 
    temp = [int(i) for i in input().split(',')]
    env.append(temp)
env = sorted(env,key = (lambda x: (x[0],x[1])))
res = 0
for i in range(len(env)):
    wide = 0
    h = 0
    temp = 0
    for j in range(i,len(env)):
        if h < env[j][1] and wide < env[j][0]:
            h = env[j][1]
            wide = env[j][0]
            temp +=1
    if temp > res:
        res = temp
print(res)