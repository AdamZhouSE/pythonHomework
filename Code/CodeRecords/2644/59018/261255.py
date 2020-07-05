info=input()[1:-1].split(',')
a=[int(y) for y in info]

K=int(input())

if sum(a)<K:
      print(-1)