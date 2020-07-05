cnt=int(input())
for i in range(0,cnt):
    str=input()
    patt=input()
    list1=list(str)
    list2=list(patt)
    flag=False
    for i in range(0,len(list1)):
        for j in range(0, len(list2)):
             if list2[j]==list1[i]:
                  print(list2[j])
                  flag=True
                  break
        if flag :
            break
if not flag:
    print("$")