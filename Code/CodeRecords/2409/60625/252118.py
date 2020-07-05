chips=input().split(',')
step = 0
for num in chips:
    if int(num) % 2 == 1:
        step += 1
print(min(step, len(chips) - step))