num=input()
answer=0
for i in range(len(num)):
    if num.count(num[i])==3:
        continue
    else:
        answer=num[i]
print(answer)