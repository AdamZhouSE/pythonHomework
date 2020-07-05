def solve(n,s):
    judge = False
    if n >=2:
        if s[0] == 'K' and s[1] == 'K':
            judge = True
        if s[n-1] == 'V' and s[n-2] == 'V':
            judge = True
    
    current = s[0]
    count = 0
    tag = 1
    i = 1
    while i < len(s):
        if not judge and current == s[i]:
            tag += 1
            if tag == 3:
                judge = True
        if not judge and current != s[i]:
            tag = 1
            current = s[i]
        if s[i] == 'K' and s[i-1] == 'V':
            count += 1
        i += 1
    
    if judge:
        count += 1
    
    print(count,end = "")

#main-----
n = int(input())
s = input()

solve(n,s)

