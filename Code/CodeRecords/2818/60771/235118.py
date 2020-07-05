#4
l = input().split(" ")
n = int(l[0])
x = int(l[1])
ci = []
l = input().split(" ")
for i in l:
    ci.append(int(i))
ci.sort()
sum = 0
while len(ci)>0:
    sum = sum + x*ci[0]
    ci.remove(ci[0])
    if(x>1):
        x = x-1
print(sum)