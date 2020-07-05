n=int(input())
array = list(map(int, input().split(" ")))
su = 0
ma = array[0]
for i in range(0, n):
    su += array[i]
    if array[i] > ma:
        ma = array[i]
if su % 2 == 1:
    print(False)
elif ma > su % 2:
    print(False)
print(True)
