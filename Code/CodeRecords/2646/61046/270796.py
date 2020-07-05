num = int(input())
s=[]
for i in range(num):
    temp = input()
    s.append(temp)

for i in range(num):
    temp = int(s[i])
    if temp%2 ==1:
        print("Player A")
    else:
        print("Player B")