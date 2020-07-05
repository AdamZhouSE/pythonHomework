n= int(input())
li = input().split()
ans = []
m = int(input())
for i in range(m):
    start,end=[int(x) for x in input().split()]
    print(len(set(li[start-1:end])))