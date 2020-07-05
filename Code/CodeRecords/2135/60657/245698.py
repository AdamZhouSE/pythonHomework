n=input().split(',')
n=[int(i) for i in n]
avr=sum(n)//len(n)
count = 0
n.sort()
for i in n:
    count += abs(n[len(n) // 2] - i)
print(count)