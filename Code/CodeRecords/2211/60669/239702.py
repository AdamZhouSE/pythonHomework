

line1=input()
strNum=int(line1.split(" ")[0])
interstNum=int(line1.split(" ")[1])

name=""
for i in range(0, strNum):
    temp=input()
    name+=(temp.split(" ")[0])
name=''.join(reversed(name))    # 字符串反转

interst=[]
for i in range(0,interstNum):
    interst.append(input())

result=[]
for string in interst:
    if len(string)==1 or string[0]!=string[-1]:  # 字符串头尾是否一样
        result.append(name.count(string))
        # 字符串的count有 连着的重复字符 的时候会出现问题【估计是判定完出现一次后会把这个字符删掉再往下找】
        # "1111".count("11")是2而不是3
    else:
        index=0
        time=0
        while True:
            if len(name)-index < len(string):
                break
            if name[index]==string[0]:
                if name[index:index+len(string)]==string:
                    time+=1
            index+=1
        result.append(time)

for item in result:
  print(item)

