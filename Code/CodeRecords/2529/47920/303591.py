import collections

n = int(input())
#print(n)
counter1 = collections.Counter(str(n))
length = len(str(n))
num = 1
flag = True
while len(str(num))<length:
    num *= 2
while len(str(num)) == n:
    if collections.Counter(str(num)) == counter1:
        flag = False
        print("true")
        break
if(flag):
    print("false")

