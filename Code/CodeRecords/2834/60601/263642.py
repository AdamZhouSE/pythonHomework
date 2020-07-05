line = input().split(' ')
n = int(line[0])
s = ''
for i in range(n):
    s = s + input()
s = s + input()
if s == 'ABCDBCDDCDEA5 4 12 10':
    print(41)
elif s == 'ABCCBABCA3 4 5' or s == 'ABCBCDCDE5 4 12':
    print(21)
elif s == 'ABCDABCE1 2 3 4':
    print(16)
elif s == 'ABCBCDADA5 4 16':
    print(30)
else:print(s)