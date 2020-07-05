n, m = map(int, input().split())
numlist = list(map(int,input().split()))
for times in range(m):
    operation = list(map(int, input().split()))
    l = operation[1]-1
    r = operation[2]-1
    if operation[0] == 0:
        numlist = numlist[0:l + 1] + sorted(numlist[l:r + 1]) + numlist[r:]
    else:
        numlist = numlist[0:l + 1] + sorted(numlist[l:r + 1])[::-1] + numlist[r:]

q = int(input())-1
print(numlist[q])
