s = input()
t = input()

map_t = {}.fromkeys(set(map(str,t)),0)
for i in range(len(t)):
    map_t[t[i]]+=1
map_s = {}.fromkeys(set(map(str,t)),0)
left = 0
right = -1
count = 0
valid = []
while left < len(s):
    if right+1 < len(s) and count < len(t):
        right += 1
        if s[right] in map_s.keys():
            map_s[s[right]]+=1
            if map_s[s[right]] <= map_t[s[right]]:
                count += 1
    else:
        if count == len(t):
            valid.append(s[left:right+1])
        if s[left] in map_s.keys():
            map_s[s[left]] -= 1
            if map_s[s[left]] < map_t[s[left]]:
                count -= 1
        left += 1
if valid:
    valid = sorted(valid, key=len)
    print(valid[0])
else:
    print('')