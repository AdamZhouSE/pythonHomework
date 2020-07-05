s = input()
s = s.replace('[', '')
s = s.replace(']', '')
s = s.split(',')
# linked_list = []
# for e in s:
#     if e.isdigit():
#         linked_list.append(int(e))
s = [int(x) for x in s]
s.sort()
print(s)