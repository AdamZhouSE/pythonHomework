import heapq
read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

ns = eval(input())
n = read()
print(heapq.nlargest(n, ns)[-1])
