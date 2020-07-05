import ast
lists1 = ast.literal_eval(input())
#print(lists1)
compare = sorted(lists1)
#print(compare)

res = 0
head = 0
tail = lists1.__len__()-1
begin = 0
end = lists1.__len__()-1
while head != tail:
    if int(lists1[head]) == int(compare[head]) and int(lists1[tail]) == int(compare[tail]):
        head = head+1
        tail = tail-1
    elif int(lists1[head]) == int(compare[head]) and int(lists1[tail]) != int(compare[tail]):
        head = head+1
        end = tail
    elif int(lists1[head]) != int(compare[head]) and int(lists1[tail]) == int(compare[tail]):
        tail = tail-1
        begin = head
    elif int(lists1[head]) != int(compare[head]) and int(lists1[tail]) != int(compare[tail]):
        begin = head
        end = tail
        break
res = end - begin +1
print(res)