import re
list=[int(x) for x in re.sub(r'[\[\],]',' ',input()).split()]
list.sort()
print(list)
