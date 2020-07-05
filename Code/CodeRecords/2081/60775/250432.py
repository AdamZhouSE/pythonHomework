X = input()
Y = input()
result = 0

if len(X) >= len(Y):
    for i in range(len(X)-len(Y)+1):
        if X[i:i+len(Y)] == Y:
            result += 1

print(result,end = '')