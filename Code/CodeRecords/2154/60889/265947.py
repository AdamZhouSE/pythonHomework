num = str(input())
for i in range(int((len(num)+1)/2)):
    if num[i] != num[len(num)-i-1]:
        print(False)
        break
else:
    print(True)
    