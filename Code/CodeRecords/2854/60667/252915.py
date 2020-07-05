li = list(map(int, input().split()))
re = []
leg = 0
for i in li:
    if i not in re:
        re.append(i)
for i in re:
    if li.count(i) >= 4:
        leg = i

if leg == 0:
    print('Alien')
    quit()
        
for i in range(4):
    li.remove(leg)
    
if li[0] == li[1]:
    print('Elephant')
else:
    print('Bear')