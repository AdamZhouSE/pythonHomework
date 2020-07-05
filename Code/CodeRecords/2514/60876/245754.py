s=list(input())
t=list(input())
start=0
end=len(t)
jud=True
for item in s:
    if item in t:
        try:
            start = t.index(item, start, end)
        except EOFError:
            jud = False
            break
    else:
        jud=False
        break
print(jud)
