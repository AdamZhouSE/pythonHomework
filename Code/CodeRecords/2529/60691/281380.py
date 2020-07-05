import itertools

def ispow(n):
    if n == 1:
        return True
    elif n%2 == 1:
        return False
    else:
        while n%2 == 0:
            n = n / 2

        if n == 1.0:
            return True
        else:
            return False

s = input()

l = []
for i in range(len(s)):
    l.append(s[i])

l1 = list(itertools.permutations(l))

boolean = False

for i in range(len(l1)):
    if l1[i][0] == '0':
        continue
    if ispow(int(''.join(list(l1[i])))):
        boolean = True
        break

if boolean:
    print('true')
else:
    print('false')

