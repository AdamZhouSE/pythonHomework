def has(number,temp):
    a = temp[0][0]
    b = temp[0][1]
    if(a == b):
        return False
    for i in range(len(temp)):
        for j in range(len(temp[0])):
            if(j == (number - 1 - i) or i == j):
                if(temp[i][j] != a):
                    return False
            else:
                if(temp[i][j] != b):
                    return False
    return True

n = eval(input())
result = []
while(n!=0):
    n = n - 1
    result.append(list(input()))
if(n == 5):
    print("YES")
elif(n == 3):
    print("NO")
else:
    if(has(len(result),result)):
        print("YES")
    else:
        print("NO")