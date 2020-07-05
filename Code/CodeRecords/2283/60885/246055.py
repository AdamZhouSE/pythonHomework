def test():
    N = int(input())
    nums = list(map(str, sorted(list(map(int, input().split())))))
    result.append(' '.join(nums))
    

result = []
for i in range(int(input())):
    test()

for i in result:
    print(i)