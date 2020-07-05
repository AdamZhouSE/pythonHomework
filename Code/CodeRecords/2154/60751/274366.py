num=input()
a=True
for i in range(len(num)//2):
    if num[i]!=num[len(num)-1-i]:
        a=False
print(a)
