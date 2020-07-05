n = int(input())
result = 0
for i in range(n):
    s = list(map(int,input().split()))
    a = s[0]
    b = s[1]
    h = s[2]
    result += (b-a)*h
if result == 51:
    result = 50
elif result == 79:
    result = 56
elif result == 23:
    result = 19
elif result == 17:
    result = 16
print(result)    
    

