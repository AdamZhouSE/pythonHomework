num=int(input())
list_name=[]
list_ans=[]
for i in range(num):
    list_name.append(input())
for name in list_name:
    set_name=set(name).difference({'a','e','i','o','u'})
    if len(set_name)%2==0:
        list_ans.append("SHE!")
    else:
        list_ans.append("HE!")
print("\n".join(str(i) for i in list_ans))