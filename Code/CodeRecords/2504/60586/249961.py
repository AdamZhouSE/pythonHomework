import re
X = re.split('\D', input())
X.remove('\D')
print(X)