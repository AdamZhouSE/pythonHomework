info=input()[1:-1].split(',')
a=[int(y) for y in info]
print(a)
print(input())
print(K)
if sum(a)<K:
      print(-1)