i = input()
n = input()
li = i.split(',')

for i in range(len(li)):
    if li[i]==n:
        print(i)
    elif i==len(li)-1:
        print(len(li))
    elif int(li[i]) < int(n) and int(n) < int(li[i+1]):
        print(i)