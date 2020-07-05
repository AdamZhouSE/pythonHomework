word=raw_input()
num=list(int(r) for r in word.split())
l=len(num)
num1=[]
for i in range(l-1):
    num1.append(num[l-1-i])
for i in range(l-1):
    if l==2:
        print(num1[0])
        break
    print(num1[i])