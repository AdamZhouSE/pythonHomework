def print_(num,result):
    if num>1:
        a=str(num)+" "+result
        print_(num-1,a)
    else:
        print("1 "+result)

num=int(input())
for i in range(num):
    print_(int(input()),"")
