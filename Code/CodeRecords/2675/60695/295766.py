t = int(input())
for i in range(t):
    n = input()
    m = 0
    for j in range(len(n)):
        if n[j]=='6':
            m = m * 10 + 9
        else:
            m = m * 10 + int(n[j])
    print(m-int(n))