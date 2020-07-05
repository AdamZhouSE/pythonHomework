num=eval(input())
i=0
while i<len(num)-1:
    if num[i]!=num[i+1]:
        print(num[i])
        break
    i=i+2
