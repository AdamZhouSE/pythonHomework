n=int(input())
for i in range(n):
    class Larger(str):
        def __lt__(x, y):
            return x+y > y+x
    input()
    result=sorted(map(str, input().split()), key=Larger)
    print(''.join(result))
