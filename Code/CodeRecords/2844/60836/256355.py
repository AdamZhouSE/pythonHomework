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

num_of_book=0
while spare_time>min(time_of_book) and len(time_of_book)>0:
    spare_time=spare_time-min(time_of_book)
    num_of_book=num_of_book+1
    del time_of_book[time_of_book.index(min(time_of_book))]

print(num_of_book)