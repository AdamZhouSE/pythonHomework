questNum = int(input())

count = 0
for i in range(questNum):
    s = input()
    
    for w in s:
        count += s.count(w) - 1

print(count)