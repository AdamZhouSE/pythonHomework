i = input()
print(sorted(i[1:len(i)-1].split(','),reverse=True)[int(input())-1])