str = int(input())

start = 0
situation = []
for i in range(0,str):
    situation.append(0)

def switchI(number,situation):
    if situation[number-1] == 0:
        situation[number-1] = 1
    else:
        situation[number-1] = 0

while start < str:
    start += 1
    for i in range(1,str+1):
        if start*i <= str:
            switchI(start*i,situation)
        else:
            break

print(situation.count(1))
