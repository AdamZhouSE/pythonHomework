n,k = input().split(' ')
n = int(n)
k = int(k)
a = list(input().split(' '))
a = list(map(int,a))
a = sorted(a)[::-1]
hasFound = False

cnt = 0
while hasFound == False and cnt<len(a):
    if k%a[cnt] == 0:
        hasFound = True
        print(int(k/a[cnt]))
    cnt+=1