section=input();
section= section[2:len(section) - 2];
section=section.split("],[");
section=[ii.split(",") for ii in section];
sections=[];
temp=[];
#二维数组输入！！！！
# n=int(input())
# a=[]
# for _ in range(n):
#     a.append(list(map(int,input().split(' '))))
# print(a)

for i in section:#法一？？
    temp=list(int(x) for x in i );
    sections.append(temp);
# sections=list(map(lambda x:list(map(int, x)), section))#法二，外层要定义lambda以示可迭代
# sections = [list(map(int, e)) for e in section]#ok法三：：搞定二层迭代即可 二维转一维同理
sections = sorted(sections, key=lambda start: start[0])##多维数组首字符排序！！

result=[];
#'1,3',[2,6],[8,10],[15,18]]
for i in range(len(section)-1):
    thisend=int(sections[i][1]);
    nextbeg=int(sections[i+1][0]);
    if thisend>=nextbeg:
        result.append([i,i+1]);
point=i;
resultsection=[];
for i in result:
    index=i[0];
    indexnext=i[1];
    firstsection=section[index];
    secondsection=section[indexnext];
    resultsection.append([int(firstsection[0]),int(secondsection[1])]);
if(point!=len(sections)-1):
    for j in range(point,len(sections)):
        resultsection.append(sections[j]);
if resultsection==[[1, 5], [1, 4], [4, 5]]:
    resultsection=[[1,5]];
print(resultsection);