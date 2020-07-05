string=input()
n=string.__len__()
answer="CODEFESTIVAL2016"
count=0
for i in range(n):
    if string[i:i+1]!=answer[i:i+1]:
        count+=1
print(count)