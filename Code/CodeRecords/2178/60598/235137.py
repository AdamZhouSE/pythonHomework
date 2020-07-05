count = set()
times = int(input())
result = []
temp = ""
strings = input().split(" ")
for i in range(times):
    count.add(strings[i])
    for j in range(i):
        count.add("".join(strings[j:i+1]))
    print(len(count))
