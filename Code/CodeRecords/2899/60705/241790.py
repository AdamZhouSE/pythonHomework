s = set()
for i in range(0, 17):
    s.add(4**i)
n = int(input())
if s.__contains__(n):
    print("true")
else:
    print("false")