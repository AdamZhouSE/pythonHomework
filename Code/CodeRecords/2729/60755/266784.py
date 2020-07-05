string = input()
l = string[1:-1].split(",")
for i in range(len(l)):
    if l.count(l[i])==1:
        print(l[i])
        break
