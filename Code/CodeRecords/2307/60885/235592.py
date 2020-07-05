end = []

def test():
    global end
    total = int(input())
    nums = input().split(' ')

    counter = {}
    for num in nums:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1
    # print('counter: %s'%counter)
    result = (0,0)
    for num, count in counter.items():
        if count > result[1]:
            result = (num, count)
    if result[1] >= total/2:
        end.append(result[0])
    else:
        end.append(-1)

for i in range(int(input())):
    test()
for i in end:
    print(i)