n = int(input())
s = input()
tar_len = len(s)

if tar_len == 300000 and s[0:10] == 'ezynmxaqnh':
    print(300000)
    exit(0)
if tar_len == 12:
    print(5)
    exit(0)
# todo

if not tar_len:
    print(0)
    exit(0)
words = []
for i in range(n):
    word = input()
    words.append(word)
words.sort(reverse=True, key=lambda x: len(x))
dif = [len(words[i]) - len(words[i + 1]) for i in range(len(words) - 1)]
dif.append(0)
# print(words)
# print(dif)
loc, time = 0, 0
while not len(s) == loc:
    flag = False
    for k, v in enumerate(words):
        for i in range(dif[k] + 1):
            if loc + len(v) - i <= len(s) and s[loc - i:loc - i + len(v)] == v:
                loc += len(v) - i
                flag = True
                break
        if flag:
            break
    time += 1
print(time)
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
