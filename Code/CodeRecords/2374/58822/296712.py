num=int(input())
for i in range(num):
    n=int(input())
    s=input()
    r=s.split(' ')
    r=list(map(int,r))
    r.sort()
    print(r)