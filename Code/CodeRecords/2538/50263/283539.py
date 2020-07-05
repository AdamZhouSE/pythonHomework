n = eval(input())
for i in range(1,len(n)+1):
    if i not in n:
        print(i)
        break
