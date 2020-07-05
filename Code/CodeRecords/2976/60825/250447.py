s1=input()
print(s1)
for i in range(20):
    try:
        s2=input()
    except:
        break
    s2.replace(s1, '')
    print(s2)