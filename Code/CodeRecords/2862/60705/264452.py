n = int(input())
arr = list(map(int, input().split(" ")))
arr.sort()
arr.reverse()
odd = []
even = []
for i in arr:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
if abs(len(even) - len(odd)) <= 1:
    print(0)
else:
    # 奇数多，就先删奇数，这样能多删一个奇数
    if len(odd) > len(even):
        length = len(even)
        odd = odd[length+1:]
        print(sum(odd))
    else:
        length = len(odd)
        even = even[length+1:]
        print(sum(even))
