import itertools
str1 = input()
str2 = input()
lists = list(str1)
issubstring = False
for temp in itertools.permutations(lists):
    stro = ''.join(temp)
    if str2.count(stro)>=1:
        issubstring = True
        break
print(issubstring)