n = int(input())
for i in range(n):
    list1 = input().split(' ')
    k = int(list1[0])
    qidian = ord(list1[1]) - ord('a')
    input()
    matx = []
    already = []
    res=[]
    for j in range(k):
        matx.append(list(input().split(' '))[1:])
    already.append(qidian)
    while len(already)!=k:
        for j in range(k):
            if j not in already and matx[qidian][j] == '1':
                qidian = j
                already.append(qidian)
                break
    for i in range(0,len(already)):
        if i !=len(already)-1:
            print(chr(i+ord('a')),end=' ')
        else:
            print(chr(i+ord('a')))