import collections
n=int(input())
count = collections.Counter(str(n))
for b in range(31):
    tmp=collections.Counter(str(1<<b))
    if(tmp==count):
        print("true")
        break
else:
    print("false")