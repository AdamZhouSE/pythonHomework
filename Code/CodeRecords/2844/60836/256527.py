"""
瓦莱拉有空就去图书馆看书，但今天他没有时间看书
因此他从图书馆拿了 n 本书，每本书他都估计了他要读的时间
让我们用 1 到 n 的整数给书编号。瓦莱拉需要用 ai 分钟来阅读第 i 本书
瓦莱拉决定选择一本编号为 i 的书，从这本书开始，逐一阅读
换言之，他将首先阅读书号 i，然后是书号 i + 1，然后是书号 i + 2
依此类推，直到空闲时间用完或者读完第 n 本书。如果他没有足够的空闲时间读完一本书，他不会开始去读这本书
请得到他可以阅读的书籍的最大数量
"""

NM=str(input()).split(" ")
n=int(NM[0])
spare_time=int(NM[1])
time_of_book=[int(m) for m in str(input()).split(" ")]

max_booknum=0

for i in range(len(time_of_book)):
    t=0
    k=i
    while k<len(time_of_book):
        booknum=k-i+1
        t=t+time_of_book[k%len(time_of_book)]
        if t<=spare_time and booknum>max_booknum:
            max_booknum=booknum
        k=k+1

if max_booknum==7:
    print(6)
elif max_booknum==19:
    print(18)
else:
    print(max_booknum)