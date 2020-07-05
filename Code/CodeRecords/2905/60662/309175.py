n = list(map(int, input().strip('[]').split(',')))
s = 0
length = len(n)-1
i = 0
while length >= 0:
    s = s + n[length]*pow(2,i)
    i = i+1
    length-=1
print(s)
