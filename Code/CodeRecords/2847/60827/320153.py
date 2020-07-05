n = int(input())
l = [int(x) for x in input().split()]
start,end=[int(x) for x in input().split()]
print(sum(l[start-1:end-1]))
