timeline, limit = input().split()
time = list(map(int, input().split()))

words = 1
for i in range(time.__len__()-1):
    if int(time[i+1]) - int(time[i]) > int(limit):
        words = 1
    else:
        words = words+1
res = words
if res==1:
    print(0)
else:
    print(res)