num=int(input())
str_=""
i=1
while(len(str_)<=num):
    str_+=str(i)
    i+=1
print(str_[num-1])
