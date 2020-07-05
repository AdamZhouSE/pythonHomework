cnt = 0
#                           source  pattern
def parse2(source, pattern, begin, index):
    if begin == len(source):
        return
    if index == len(pattern):
        return
    global cnt
    target = pattern[index]
    # print(source[begin:])
    for i in range(begin, len(source)):
        if target == source[i]:
            if index == len(pattern) - 1:
                cnt += 1
            else:
                parse2(source, pattern, i+1, index+1)
    return

t = int(input())
liOfInputs = []
for i in range(t):
    li = input().split(" ")
    li = input().split(" ")
    liOfInputs.append(li)

for i in liOfInputs:
    cnt = 0
    # print(i[0])
    # print(i[1])
    parse2(i[0], i[1], 0, 0)
    print(cnt)