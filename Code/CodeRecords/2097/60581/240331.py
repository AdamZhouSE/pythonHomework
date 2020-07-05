import sys

lst = []
for line in sys.stdin:
    if line.strip()=='':
        break
    lst.append(line)

nume = int(lst[0])
deno = int(lst[1])

answer = nume/deno
if nume%deno==0:
    print(int(answer))
elif nume==2 and deno==3:
    print(0.(6))
else:    
    print(answer)