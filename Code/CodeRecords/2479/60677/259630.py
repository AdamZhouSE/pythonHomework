times=int(input())
for i in range(times):
    str1=input()
    str2=input()
    answer=[]
    for i in str1:
        if i not in str2:
            answer.append(i)
    for i in str2:
        if i not in str1:
            answer.append(i)
    answer=list(set(answer))
    answer.sort()
    print("".join(answer))
    print()