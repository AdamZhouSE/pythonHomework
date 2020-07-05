def do(father):
    if sons[father] == []:
        return 1
    elif len(sons[father]) == 1:
        return 1 + do(sons[father][0])
    else:
        left = do(sons[father][0])
        right = do(sons[father][1])
        return 1 + max(left,right )

num_v = int(input())

sons = [[] for i in range(num_v)]
for i in range(num_v-1):
    input1 = input().split(' ')
    father = int(input1[0])
    son = int(input1[1])
    sons[father].append(son)

print(do(0))