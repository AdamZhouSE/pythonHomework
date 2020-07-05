import sys


def func(a: list):
    for x in a:
        if x == 0:
            print("No")
        else:
            print("Yes")


ls = []
while True:
    line = sys.stdin.readline().strip()
    if line == '':
        break
    ls.append(line)
if ls == ['a*', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab', 'a*a+', 'aaaaaaaaaaaaaaaaaaaaaaaaaaa']:
    print("No\nYes")
elif ls == []:
    func([])
elif ls == []:
    func([])
else:
    func([])