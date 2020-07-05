def convert(str1,st):
    def slice(str,list):
        for i in str:
            list.append(int(i))
    list = []
    for i in range(len(str1)):
        slice(str(st+ord(str1[i])-ord('A')),list)
    return list
def cal(list):
    for i in range(len(list)-1):
        list[i] = (list[i]+list[i+1])%10
    list.pop(-1)
name = input()
st = int(input())
list = convert(name,st)
while len(list)>=3 and not (len(list) == 3 and list[0]==1 and list[1]==0 and list[2]==0):
    cal(list)
for i in range(len(list)):
    if i==0 and list[i] ==0:
        continue
    print(list[i], end="")


