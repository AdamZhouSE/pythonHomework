s=input()
s=s[1:len(s)-1]
lst=s.split(',')
list.sort(lst)
lst=list(map(int,lst))
print(lst)