import re
pattern = re.compile('-*[0-9]+')
a = [int(x) for x in pattern.findall(input())]
a.sort()
print(a[len(a)-1]*a[len(a)-2]*a[len(a)-3])



