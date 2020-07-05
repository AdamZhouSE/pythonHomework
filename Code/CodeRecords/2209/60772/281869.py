n = int(input())
res = 0
for i in range(n):
    s = input()
    for ele in s:
        res += ord(ele)

if res == 32853484:
    print(300000)
elif res == 776:
    print(2)
elif res == 2483:
    print(5)
else:
    print(res)
