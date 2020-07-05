count=int(input())
for n in range(count):
    num=int(input())
    array = [int(x) for x in input().split()]
    array.sort()
    print(*array)