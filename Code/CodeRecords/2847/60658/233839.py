n = int(input())
li = [int(x) for x in input().split()]
start,end=[int(x) for x in input().split()]
print(sum(li[start-1:end-1]))


