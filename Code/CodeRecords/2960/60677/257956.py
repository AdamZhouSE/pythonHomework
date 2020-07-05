s=input()
a=input()
b=input()
answer=[]
for i in range(b.__len__()-a.__len__()+1):
    for j in range(a.__len__()):
        judge=True
        if a[j:j+1]=="*" or b[i+j:i+j+1]=="*":
            continue
        elif a[j:j+1]!=b[i+j:i+j+1]:
            judge=False
            break
    if judge:
        answer.append(str(i+1))
print(answer.__len__())
for i in answer:
    print(i,end=" ")
print()