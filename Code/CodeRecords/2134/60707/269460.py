buckets = int(input())
m = int(input())
p = int(input())
if buckets == 0:
    print('0')
w = p / m + 1
re = 1
while pow(w, re) < buckets:
    re += 1
print(str(re))