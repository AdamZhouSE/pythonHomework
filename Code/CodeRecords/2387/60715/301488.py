n, m = map(int, input().split())
numlist = list(map(int,input().split()))
for times in range(m):
    operation = list(map(int, input().split()))
    l = operation[1]
    r = operation[2]
    if operation[0] == 0:
        numlist = numlist[0:l-1] + sorted(numlist[l-1:r]) + numlist[r:]
    elif operation[0] == 1:
        numlist = numlist[0:l-1] + sorted(numlist[l-1:r])[::-1] + numlist[r:]
q = int(input())-1
print(numlist[q])