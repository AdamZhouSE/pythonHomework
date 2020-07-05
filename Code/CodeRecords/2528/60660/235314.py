orgstr=input()[1:-1].split(',')
org=[int(orgstr[i]) for i in range(len(orgstr))]
org.sort()
print(org)