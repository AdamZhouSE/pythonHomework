import sys

lst = []
for line in sys.stdin:
    if line.strip()=='':
        break
    lst.append(line)

nume = int(lst[0])
deno = int(lst[1])

print(nume/deno)