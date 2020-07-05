N = int(input())
list1 = []
for a in range(0,N):
    source = input()
    result = ""
    for x in source:
        if x.isdigit():
            result = result+x
        elif 65<=ord(x)<=67:#ABC
            result = result+'2'
        elif 68<=ord(x)<=70:#DEF
            result = result+'3'
        elif 71<=ord(x)<=73:#GHI
            result = result+'4'
        elif 74<=ord(x)<=76:#JKL
            result = result+'5'
        elif 77<=ord(x)<=79:#MNO
            result = result+'6'
        elif 80<=ord(x)<=83:#P(Q)RS
            result = result+'7'
        elif 84<=ord(x)<=86:#TUV
            result = result+'8'
        elif 87<=ord(x)<=89:#WXY
            result = result+'9'
    result = result[0:3]+"-"+result[3:]
    list1.append(result)
flag = False
for x in range(0,len(list1)):
    if list1.count(list1[x])!=1:
        if list1.index(list1[x])==x:
            print(list1[x],end=' ')
            print(list1.count(list1[x]))
            flag = True
if not flag:
    print("No duplicates.",end='')
