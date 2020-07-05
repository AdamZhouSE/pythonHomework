n = input()
a = list(map(int, input().split()))
print('YES' if sum(a)%2==0 and 2*max(a)<=sum(a) else 'NO')