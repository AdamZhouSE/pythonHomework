a=input()
num=[int(x) for x in input().split()]
num.sort()
s=""
for i in num:
    s=s+str(i)+" "
print(s.rstrip())