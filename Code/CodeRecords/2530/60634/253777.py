S = input()
T = list(input())

result = ""
for x in S:
    i = 0
    while i < len(T):
        if x == T[i]:
            result += x
            T.remove(x)
            break
        i += 1
        
for x in T:
    resukt += x

print(result)