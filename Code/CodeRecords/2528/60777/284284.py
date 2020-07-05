temp=input()
temp=temp[1:len(temp)-1]

l=[int(x) for x in temp.split(',')]
l.sort()

print(l)