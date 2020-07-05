
def pair():
    boys = int(input())
    b_skills = list(map(int,input().split(' ')))
    girls = int(input())
    g_skills = list(map(int,input().split(' ')))
    b_skills.sort()
    g_skills.sort()
    i = 0
    j = 0
    res = 0
    last_j = 0
    while i < len(g_skills):
        success = False
        while j < len(b_skills):
            if abs(g_skills[i] - b_skills[j]) <= 1:
                res += 1
                i = i +1
                j += 1
                success = True
                last_j = j
                break
            else:
                j += 1
        if not success:
            i = i + 1
            j = last_j
        if j == len(b_skills):
            break
    print(res)
    return

pair()