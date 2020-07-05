a = [int(i) for i in input().split(',')]
overall = 0
seg = 0
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            if j==i+1:
                seg += 1
                overall += 1
            else:
                overall += 1
if overall==seg:
    print('True')
else:
    print('False')