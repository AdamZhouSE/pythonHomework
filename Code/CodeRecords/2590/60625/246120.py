num = int(input())

for i in range(num):
    a = ''

    ID = input()
    Only_ID = str(set(ID))

    res='HE!'
    New_Only_ID=Only_ID.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')
    if len(New_Only_ID)%2==0:
        res='S'+res
    print(res)