import collections

N = int(input())
#print(n)
n = str(N)
c = collections.Counter(n)
leng = len(n)
i = 0
flag = False
while 2 ** i < 10 ** leng:
    a = collections.Counter(str(2 ** i))
    if a == c:
        flag = True
        break
    i += 1
if(flag):
    print("true")
else:
    print("false")