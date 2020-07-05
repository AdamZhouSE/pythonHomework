s = input().strip()
s = s.split(' ')
s.sort(key = lambda i:len(i),reverse=True)
print(s[0])