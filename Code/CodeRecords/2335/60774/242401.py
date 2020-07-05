a = int(input())
b = int(input())
bRef = [b]
bRem = [0]
aRef = [a]
while(b > a):
    bRem.insert(1,int(b % 2))
    if(b % 2):
        b = (b + 1) / 2
    else:
        b = b / 2
    bRef.insert(0,int(b))
b = bRef[-1]
while(a < b):
    a = a * 2
    aRef.append(a)
a = aRef[-1]
ref = []
for i in range(0,len(bRef)):
    ref.append(aRef[i] - bRef[i])
node = ref.index(min(ref))
count = min(ref) + len(ref) - 1 + sum(bRem[node + 1:])
print(count)