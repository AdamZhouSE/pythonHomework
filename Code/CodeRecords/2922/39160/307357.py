n = input()
a = sorted(set(map(int, input().split())))
print('YES' if len(a)<=2 or len(a)==3 and a[2]-a[1] == a[1]-a[0] else 'NO') 