import sys

lst = []
for line in sys.stdin:
    if line.splice()=='':
        break
    lst.append(line)

nume = int(lst[0])
deno = int(lst[1])

print(nume/deno)