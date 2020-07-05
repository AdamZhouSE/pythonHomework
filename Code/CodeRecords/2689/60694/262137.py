T = int(input())
for _ in range(T):
    str1, str2 = input().split()
    c = len(set(str1) & set(str2))
    print(len(str1) + len(str2) - c)
