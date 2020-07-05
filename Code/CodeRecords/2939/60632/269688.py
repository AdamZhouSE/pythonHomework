try:
    s = input()
    k, m = map(int, s.split(' '))
except ValueError as e:
    k, m = map(int, s.split('  '))
queue = [1]
target = []
while len(target) < k:
    queue.append(2 * queue[0] + 1)
    queue.append(4 * queue[0] + 5)
    target.append(str(queue[0]))
    del queue[0]
    queue = sorted(queue)
target = list(''.join(target))
print(''.join(target))
n = len(target) - m  # n为最后留下的数字个数
result = ''
while n > 0:
    op = max(target[:m + 1])
    result += op
    m -= target.index(op)
    target = target[target.index(op) + 1:]
    n -= 1
print(result, end='')
