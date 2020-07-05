# 3
inp = input()
inp = input()
p_score = inp.split()

all_score = []

for i in p_score:
    if i in all_score:
        continue
    else:
        all_score.append(i)
if '0' in all_score:
    print(len(all_score) -1)
else:
    print(len(all_score))