num=int(input())
string=input()
count=0
for i in range(num-1):
    if string[i]==string[i+1]:
        count=count+1
print(count)