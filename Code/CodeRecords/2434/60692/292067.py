n_m_c = input().split(' ')
n = int(n_m_c[0])
m = int(n_m_c[1])
c = int(n_m_c[2])
ans = []
sound = input().split(" ")
sound = [int(i) for i in sound]
i = 0
while i <= len(sound) - m:
    if max(sound[i:i+m]) - min(sound[i:i + m]) <= c:
        ans.append(i + 1)
    i += 1
if not ans:
    print("NONE")
else:
    for i in ans:
        print(i)
