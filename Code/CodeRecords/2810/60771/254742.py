#41
num = int(input())
outcome = []
while num > 0:
    if num < 10:
        for i in range(0,num):
            outcome.append(1)
        break
    break

print(len(outcome))
for i in range(0,len(outcome)-1):
    print(outcome[i],end=" ")
print(outcome[len(outcome)-1])