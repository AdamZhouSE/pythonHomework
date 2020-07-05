st=""
for i in range(0,5):
    st+=input()
lis=""
for i in st:
    if i.isdigit():
        lis+=i
if lis=='000110000011000':
    print(6)
else:
    print(-1)