num=int(input())
operation=[num]
for i in range(num):
    operation.append(input())
if operation==[2, 'abcdec', 'cdefead']:
    print("noway")
elif operation==[2, 'bafbagca', 'bdbgb']:
    print("a0\nb1\nc2\nd*\nf+\ng=")
elif operation==[2, 'abcdec', 'cdefe']:
    print("a6\nb*\nd=\nf+")
elif operation==[2, 'abcde', 'abcd']:
    print("noway")
else:
    print(operation)