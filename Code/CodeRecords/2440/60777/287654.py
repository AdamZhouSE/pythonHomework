temp=input()
temp=temp[1:len(temp)-1]
temp=[int(x) for x in temp.split(',')]
temp.sort()
print(temp)
