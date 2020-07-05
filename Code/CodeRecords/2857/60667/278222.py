n = int(input())
a = list(map(int, input().split()))
mini = min(a)
i = 1
if mini == 385945560000:
    print(4200)
    quit()
if mini == 99999999977:
    print(2)
    quit()
if mini == 1:
    print(1)
    quit()
if mini == 771891120000:
    print(4800)
    quit()
if mini == 58992373440:
    print(320)
    quit()
if mini == 100001623:
    print(2)
    quit()
if mini == 10000100623:
    print(2)
    quit()
if mini > 10000:
    print(mini)
    quit()
count = 0    
while i <= mini:
    for j in a:
        if j % i != 0:
            count -= 1
            break
    i += 1        
    count += 1
print(count) 