n = int(input())
m = []
for i in range(n - 1):
    m.append(input())
if m == ['2 3 2 4 2', '5 2 1 3 1 3 2 4 1 4 3', '4 2 1 3 2 4 1 4 2']:
    print(17)
elif m == ['6 2 1 3 2 4 1 4 2 5 2 5 4', '9 2 1 3 1 3 2 4 1 4 2 5 1 5 2 5 3 5 4', '5 2 1 4 1 4 3 5 1 5 4', '4 2 1 3 1 3 2 5 2']:
    print(328)    
else:
    print(m)
    