n = int(input())
w_count = 1
t_set = set()
for i in range(n):
    time = input()
    if time in t_set:
        w_count += 1
    t_set.add(time)
print(w_count)
