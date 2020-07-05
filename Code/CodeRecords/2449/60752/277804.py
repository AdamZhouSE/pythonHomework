ip=input()

lst=eval(ip)
find=input()
found=False
for i in range(len(lst)):
    if lst[i]==int(find):
        print(i)
        found=True
        break
if not found:
    print(-1)
