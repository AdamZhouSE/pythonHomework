
def do():
    all = []
    times = []
    for i,n in enumerate(nums):
        if n not in all:
            all.append(n)
            times.append(1)
        else:
            times[all.index(n)] += 1
    for i,n in enumerate(times):
        if n % 2 == 1:
            print(all[i])
            return
    print(0)
    return

num_tests = int(input())
for i in range(num_tests):
    amount = int(input())
    nums = [int(n) for n in input().split(' ')]
    do()