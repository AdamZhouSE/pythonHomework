tests = int(input())

lists = []
for i in range(tests):
    temp = int(input())
    lists.append(temp)
#print(lists)

def fib(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a

for i in range(lists.__len__()):
    print(fib(lists[i]+1))