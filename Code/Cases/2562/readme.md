### 题目描述
Hattori受到GMAIL工作方式的极大启发。他决定构建自己的简单版本的GMAIL。他将邮件分为3类，即：UNREAD，READ和TRASH。 

未读：未读的消息。 

阅读：用户阅读的消息。 

TRASH：用户删除的消息。 

现在，在任何时间点，用户都可以读取UNREAD消息，将UNREAD消息移至TRASH，将READ消息移至TRASH或将已删除的消息恢复为READ类别。

现在，Hattori需要您的帮助来确定所有类别中剩余的邮件，按照它们到达该类别的顺序进行排列。 

形式上：给您N条消息，ID从1到N。最初，所有消息都在邮件的UNREAD部分中。

现在，Q查询的形式如下所示： 

1 X：将ID为X的消息从UNREAD移到READ。 

2 X：将ID为X的消息从READ移到TRASH。 

3 X：将ID为X的消息从UNREAD移到TRASH。 

4 X：将ID X的消息从TRASH移到READ。 

鉴于所有查询均有效，请帮助Hattori确定所有3部分中的消息。
### 输入描述
第一行包含测试用例的数量。每个测试用例的第一行分别包含两个以空格分隔的值N和Q。第二行包含2 * Q个整数，每种形式如上所述。
### 输出描述
第一行包含UNREAD部分中所有用空格分隔的消息ID。 

第二行包含READ部分中剩余的所有空格分隔的消息ID。 

第三行包含TRASH部分中所有用空格分隔的消息ID。 

注意：如果任何部分为空，请为该部分打印“ EMPTY”，而不用双引号引起来。
### 输入范例
```
1
10 7
1 2 1 5 1 7 1 9 2 5 2 7 4 5
```
### 输出范例
```
1 3 4 6 8 10 
2 9 5 
7
```
### 题目来源
geeksforgeeks.org