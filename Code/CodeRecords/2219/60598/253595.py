num = int(input())
finish = False
for i in range(num):
    for j in range(num):
        if i*i+j*j ==num:
            print(True)
            finish = True
            break
        elif i*i+j*j >num:
            break
    if finish:
        break
if not finish:
    print(False)
