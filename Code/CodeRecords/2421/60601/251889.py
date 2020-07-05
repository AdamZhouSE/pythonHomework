n = list(input())
if '6' in n:
    for i in range(len(n)):
        if n[i] == '9':continue
        else:
            n[i] = '9'
            break
print(''.join(n))