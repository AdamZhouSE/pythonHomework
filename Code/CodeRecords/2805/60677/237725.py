n=int(input())
line=input().split()
line=[int(x) for x in line]
answer=[]
count=1
for i in range(n-1):
    if line[i+1]>line[i]:
        if i==n-2:
            answer.append(count+1)
            break
        count += 1
    else:
        answer.append(count)
        count=1
answer.sort(reverse=True)
if answer.__len__()!=0:
    print(answer[0])
else:
    print(1)