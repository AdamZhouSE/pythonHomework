str = input()
li = str.split(',')
for i in range(len(li)):
    if i==len(li)-1:
        print(i)
    if int(li[i-1]) < int(li[i]) and int(li[i+1]) < int(li[i]):
        print(i)
        break