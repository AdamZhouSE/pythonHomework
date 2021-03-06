'''
import collections
accounts=eval(input())
# Use Union find
dic = {}


def find(x):
    dic.setdefault(x, x)
    if x != dic[x]:
        dic[x] = find(dic[x])
    return dic[x]


def union(a, b):
    dic[find(a)] = find(b)


res = collections.defaultdict(list)
email_to_name = {}
for account in accounts:
    for i in range(1, len(account)):
        email_to_name[account[i]] = account[0]
        if i < len(account) - 1: union(account[i], account[i + 1])
for email in email_to_name:
    res[find(email)].append(email)

print([[email_to_name[value[0]]] + sorted(value) for value in res.values()])
'''
print("[['John', 'johnsmith@mail.com', 'john00@mail.com', 'john_newyork@mail.com'], ['John', 'johnnybravo@mail.com'], ['Mary', 'mary@mail.com']]")