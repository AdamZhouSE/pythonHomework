nums=input().split(",")
threshold=int(input())
sum=0
for i in nums:
    sum=sum+int(i)
og=sum//threshold

def div(a,b):
    if a/b==float(a//b):
        return a//b
    else:
        return a//b+1

answer=sum
while(answer>threshold):
    answer=0
    for i in nums:
        answer=answer+div(int(i),og)
    og=og+1
print(og-1)