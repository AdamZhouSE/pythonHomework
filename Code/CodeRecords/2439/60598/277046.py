num = int(input())
store = [[] for i in range(num + 1)]
for i in range(num - 1):
    temp = input().split(" ")
    store[int(temp[0])].append(int(temp[1]))
    store[int(temp[0])].append(int(temp[2]))


def cal(F, T, W):
    if T == F:
        return W
    if T == store[F][0]:
        return W ^ store[F][1]
    else:
        return cal(store[F][0], T, W ^ store[F][1])


question = int(input())
for j in range(question):
    temp = input().split(" ")
    print(cal(int(temp[0]), int(temp[1]), 0))
