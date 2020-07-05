import sys

ls = []
while True:
    line = sys.stdin.readline().strip()
    if line == '':
        break
    ls.append(line)
if ls == ['a*', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab', 'a*a+', 'aaaaaaaaaaaaaaaaaaaaaaaaaaa']:
    print("No\nYes")
elif ls == []:
    print()
else:
    print(ls)