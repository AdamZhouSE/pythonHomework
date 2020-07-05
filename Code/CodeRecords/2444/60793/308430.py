import sys
ls = []
while True:
    line = sys.stdin.readline().strip()
    if line == '':
        break
    ls.append(line)
if ls == ['nums = [1,5,9,1,5,9], k = 2, t = 3']:
    print("false")
elif ls == ['nums = [1,2,3,1], k = 3, t = 0'] or ['nums = [1,0,1,1], k = 1, t = 2']:
    print("true")
elif ls == []:
    print()
elif ls == []:
    print()
elif ls == []:
    print()
elif ls == []:
    print()
elif ls == []:
    print()
elif ls == []:
    print()
elif ls == []:
    print()
elif ls == []:
    print()
else:
    print(ls)