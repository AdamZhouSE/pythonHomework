str=input()
a=str.split()[0]
b=str.split()[1]
judge=True
for i in range(len(a)):
    if a[i]!=b[i]:
        print(ord(a[i])-ord(b[i]))
        judge=False
        break
if judge:
    print("0")