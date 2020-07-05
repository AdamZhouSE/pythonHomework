buckets = int(input())
die = int(input())
test = int(input())
times = test//die + 1

x = 1
while pow(times,x) < buckets:
    x += 1
print(x)