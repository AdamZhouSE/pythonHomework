def process(k):
    if k<=2:
        return 1
    return process(k-2)+process(k-3)
n=int(input())
for i in range(n):
    k=int(input())
    print(process(k))