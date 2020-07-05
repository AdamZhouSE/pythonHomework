n = int(input())
for i in range(n):
    s=list(input())
    set1=()
    for j in range(len(s)):
        if s[j]!='a' or s[j]!='o' or s[j]!='e' or s[j]!='i' or s[j]!='u':
            set1.add(s[j])
    if len(set1)%2==0:
        print('SHE!')
    else:
        print('HE!')