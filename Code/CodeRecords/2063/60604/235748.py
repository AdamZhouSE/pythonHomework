a=input()
l=len(a)

jud=True
for i in range(l):
    if not(a[i]==a[l-1-i]):
        jud=False
print(jud)