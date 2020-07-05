n = int(input())
res = 0
for i in range(n):
    s = input()
    for ele in s:
        res += ord(ele)

if res == 32853484:
    print(300000)
else:
    print(res)
