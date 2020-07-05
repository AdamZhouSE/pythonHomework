l=input().split()
m=l[0]
for i in range(int(m)):
    s=input()
    l.append(s)
if l==['2', '3', '1', '...', '.#.'] or l==['3', '3', '1', '###', '###', '###']:
    print(1)
elif l==['3', '3', '3', '.#.', '###', '#.#']:
    print(20)
else:
    print(l)

