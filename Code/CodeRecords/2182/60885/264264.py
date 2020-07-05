def find_free(n,k):
    queue = [i for i in range(1,n+1)]
    i = 0
    while len(queue) > 1:
        i = (i + k - 1) % len(queue)
        queue.remove(queue[i])
    return queue[0]

def test():
    n,k = list(map(int, input().split()))
    result.append(find_free(n,k))

result = []
for i in range(int(input())):
    test()

for i in result:
    print(i)