num = int(input())
str = input().split(' ')
lens = [ int(i) for i in str]
lens.sort()
keys = []
need1 = num//2
need2 = num-need1
key1 = 0
for i in range(need1):
    key1 = key1+lens[i]
key2 = 0
for i in range(need2):
    key2 = key2+lens[need1+i]
answer = key1**2+key2**2
print(answer)