li = [int(x) for x in input().split(",")]
k = int(input())
print(max(0,max(li)-min(li)-k*2))