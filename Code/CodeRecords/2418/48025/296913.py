tomato_num=int(input())
total_num=int(input())
a=tomato_num-2*total_num
if(a<0):
    print('[]')
elif(a%2!=0):
    print('[]')
else:
    result=[]
    result.append(int(a/2))
    result.append(int(total_num-a/2))
print(result)