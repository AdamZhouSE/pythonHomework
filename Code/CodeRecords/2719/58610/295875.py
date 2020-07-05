meet = []
for _ in range(eval(input())):
    s = input()
    if s[0] == 'A':
        a, b = list(map(int, s.split(' ')[1:]))
        count = 0
        new_meet = []
        for t in meet:
             if t[1] < a or t[0] > b:
                new_meet.append(t)
        print(len(meet) - len(new_meet))
        new_meet.append((a, b))
        meet = new_meet
    elif s[0] == 'B':
        print(len(meet))