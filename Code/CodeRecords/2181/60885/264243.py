def test():
    x = int(input())
    result.append(pow(x,3)+x)

result = []
for i in range(int(input())):
    test()

for i in result:
    print(i)