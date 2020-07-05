boys = int(input())
skill_boys = [int(x) for x in input().split()]
girls = int(input())
skill_girls = [int(x) for x in input().split()]
skill_boys.sort()
skill_girls.sort()
ans = 0
for boy in skill_boys:
    i = 0
    while i < len(skill_girls):
        if -1 <= boy-skill_girls[i] <= 1:
            ans += 1
            skill_girls.pop(i)
            break
        else:
            i += 1
print(ans)
