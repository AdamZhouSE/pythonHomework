sca = list(map(int,input()[1:-1].split(',')))
result = sca[0]
for i in range(sca[0] + 1,sca[1] + 1):
    result = result & i
print(result)