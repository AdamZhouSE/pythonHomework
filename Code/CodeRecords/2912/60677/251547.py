string=input()
n=string.__len__()
answer=1
for i in range(0,n-1):
    for j in range(i+1,n):
        seg=string[i:j]
        if seg.__len__()==set(seg).__len__() and seg.__len__()>answer:
            answer=seg.__len__()
print(answer)