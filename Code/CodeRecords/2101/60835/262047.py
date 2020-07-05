num = input()
seen = set()
result = False
while num not in seen and not result:
    
    seen.add(num)
    cnt = 0
    for x in range(len(num)):
        cnt = cnt + int(num[x])**2
    if cnt == 1:
        result = True
    num = str(cnt)
print(result)
        
        