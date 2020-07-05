a = eval(input())
bucket = [0 for i in range(max(a)+1000)]
for i in a:
    bucket[i] = 1
for i in range(len(bucket)):
    if bucket[i] != 1 and i != 0:
        print(i)
        break

