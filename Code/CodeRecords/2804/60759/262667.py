from re import findall
formula = input()
lst = findall('\d', formula)
lst.sort()
print('+'.join(lst))
