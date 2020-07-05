n = int(input())
lst = list(map(int,input().split(' ')))
odds = []
even = []
for x in lst:
    if x%2 == 0:
        even.append(x)
    else:
        odds.append(x)
odds.sort(reverse = True)
even.sort(reverse = True)

if len(even)>len(odds)+1:
    print(sum(even[len(odds)+1:]))
elif len(odds)>len(even)+1:
    print(sum(odds[len(even)+1:]))
else:
    print('0')