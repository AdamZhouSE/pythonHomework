yard = int(input().split(' ')[1])
buckets = sorted(list(map(int, list(input().split(' ')))), reverse=True)
for i in buckets:
    if yard % i == 0:
        print(yard // i)
        break