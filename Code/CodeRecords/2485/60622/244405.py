def equal(str1,str2):
    return set(str1)==set(str2)

num=int(input())
list_fin_ans=[]
for i in range(num):
    list_ans = []
    num_words=int(input())
    list_words=input().split()
    list_set=[]
    for word in list_words:
        list_set.append(set(word))
    while(len(list_set)!=0):
        times=list_set.count(list_set[0])
        list_ans.append(times)
        for i in range(times):
            list_set.remove(list_set[0])
    list_ans.sort()
    list_fin_ans.append(list_ans)

for list in list_fin_ans:
    print(" ".join(str(i) for i in list))


