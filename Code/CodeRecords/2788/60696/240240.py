n = int(input())
boy_skill = [int(i) for i in input().split()]
m = int(input())
girl_skill = [int(i) for i in input().split()]

pairs = 0

for i in boy_skill:
    if len(girl_skill) == 0:
        break
    best_buddy_skill = girl_skill[0]
    for j in range(1, len(girl_skill)):
        if abs(girl_skill[j] - i) <= min(1, abs(best_buddy_skill - i)):
            best_buddy_skill = girl_skill[j]
    if abs(best_buddy_skill - i) <= 1:
        pairs += 1
        girl_skill.remove(best_buddy_skill)

print(pairs)