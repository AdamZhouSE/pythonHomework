num=input()
sign=False
if num[0]=="-":
    sign=True
    num=num[1:len(num)]
result=""
for i in num:
    result=i+result
result=str(int(result))
if not sign:
    print(result)
else:
    print("-"+result)