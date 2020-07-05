n = int(input())
s = input()


A = ['a','b','c','d','e','f','g','h',
       'i','j','k','l','m','n','o','p','q',
       'r','s','t','u','v','w','x','y','z']


def cal(t):
    for i in range(len(A)):
        if A[i] == t:
            break
    return A[(i+n)%26]


res = list()
for i in range(len(s)):
    res.append(cal(s[i]))
print(''.join(res), end='')

