import sys

lst = []
for line in sys.stdin:
    if line.strip()=='':
        break
    lst.append(line)

nume = int(lst[0])
deno = int(lst[1])

if nume%deno==0:
    print(int(nume/deno))
else:
    print(nume/deno)