n = int(input())
s = input()
tar_len = len(s)
if not tar_len:
    print(0)
    exit(0)
words = []
for i in range(n):
    word = input()
    words.append(word)
have = set()
# print(words)
queue, time = [('', 0)], 0
while queue:
    time += 1
    for _ in range(len(queue)):
        state, loc = queue.pop()
        for p in words:
            if s[loc:loc + len(p)] == p:
                new_state = state + p
                if new_state in have:
                    continue
                have.add(new_state)
                new_len = len(new_state)
                if tar_len == new_len:
                    print(time)
                    exit(0)
                queue.insert(0, (new_state, new_len))
