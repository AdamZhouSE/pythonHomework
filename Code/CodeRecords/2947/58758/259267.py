n = int(input())
ans = []
String = input()
for i in range(0, n):
    operation = input().split()
    if operation[0] == '1':
        String += operation[1]
        ans.append(String)
    elif operation[0] == '2':
        a = int(operation[1])
        b = int(operation[2])
        String = String[a: a+b]
        ans.append(String)
    elif operation[0] == '3':
        a = int(operation[1])
        String = String[0: a]+operation[2]+String[a:]
        ans.append(String)
    else:
        try:
            ind = String.index(operation[1])
            ans.append(ind)
        except Exception:
            ans.append(-1)
for i in ans:
    print(i)
