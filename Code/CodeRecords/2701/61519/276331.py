str=list(input().split(","))
print(str)
a = [moves[i] for i in range(len(moves)) if i % 2 == 0]
b = [moves[i] for i in range(len(moves)) if i % 2 != 0]
if [0, 0] in a and [1, 1] in a and [2, 2] in a:
    print('A')
if [2, 0] in a and [1, 1] in a and [0, 2] in a:
    print('A')
if [0, 0] in a and [0, 1] in a and [0, 2] in a:
    print('A')
if [1, 0] in a and [1, 1] in a and [1, 2] in a:
    print('A')
if [2, 0] in a and [2, 1] in a and [2, 2] in a:
    print('A')
if [0, 0] in a and [1, 0] in a and [2, 0] in a:
    print('A')
if [0, 1] in a and [1, 1] in a and [2, 1] in a:
    print('A')
if [0, 2] in a and [1, 2] in a and [2, 2] in a:
    print('A')
if [0, 0] in b and [1, 1] in b and [2, 2] in b:
    print('B')
if [2, 0] in b and [1, 1] in b and [0, 2] in b:
    print('B')
if [0, 0] in b and [0, 1] in b and [0, 2] in b:
    print('B')
if [1, 0] in b and [1, 1] in b and [1, 2] in b:
    print('B')
if [2, 0] in a and [2, 1] in a and [2, 2] in a:
    print('B')
if [0, 0] in b and [1, 0] in b and [2, 0] in b:
    print('B')
if [0, 1] in b and [1, 1] in b and [2, 1] in b:
    print('B')
if [0, 2] in b and [1, 2] in b and [2, 2] in b:
    print('B')
if len(moves)==9:
    print('Draw')
else:
    print('Pending')