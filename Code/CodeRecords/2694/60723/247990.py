def count_number(string,length):
    list=[]
    for i in range(len(string)-length+1):
        list.append(string[i:i+length])
    list.sort()
    for i in range(len(list)-1):
        if list[i]==list[i+1]:
            return list[i]
    return []
string=input()
window_length=len(string)-1
while window_length>0:
    if count_number(string,window_length)!=[]:
        print(count_number(string,window_length))
        break
    window_length=window_length-1
if window_length==0:
    print()