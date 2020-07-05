def function(n):
    result = ['0','1','2']
    if n < 3:
        return int(result[n])
    f_1 = 1
    f_2 = 2
    answer = 0
    for i in range(3,n+1):
        answer = f_1 + f_2
        f_1 = f_2
        f_2 = answer
    return answer

num = int(input())
for i in range(num):
    a = int(input())
    print(function(a))