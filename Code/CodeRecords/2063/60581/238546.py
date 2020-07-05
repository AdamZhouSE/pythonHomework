str = list(input())

judge = True

for i in range(0,len(str)):
    if str[i]!=str[len(str)-i-1]:
        judge = False

print(judge)