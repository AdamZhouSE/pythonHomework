#24
# s = bin(10)
# outcome = int(s,2)
# if outcome is str:
#     print("is str")
# else:
#     print("not")

T = int(input())
for i in range(0,T):
    outcome = []
    n = int(input())
    for num in range(1,n+1):
        s = bin(num)
        flag = True
        for j in range(0,len(s)-1):
            if s[j] == s[j+1]:
                flag = False
                break
        if flag:
            outcome.append(num)
    for j in range(0,len(outcome)-1):
        print(outcome[j],end=" ")
    print(outcome[len(outcome)-1])