### 题目描述

Farmer John为他的奶牛们订阅了Good Hooveskeeping杂志，因此他们在谷仓等待挤奶期间，可以有足够的文章可供阅读。不幸的是，最新一期的文章包含一篇关于如何烹制完美牛排的不恰当的文章，FJ不愿让他的奶牛们看到这些内容。

FJ已经根据杂志的所有文字，创建了一个字符串 S ( S 的长度保证不超过 10^6)，他想删除其中的子串 T ,他将删去 S 中第一次出现的子串 T ，然后不断重复这一过程，直到 S 中不存在子串 T 。

注意：每次删除一个子串后，可能会出现一个新的子串 T （说白了就是删除之后，两端的字符串有可能会拼接出来一个新的子串 T ）。
### 输入描述

```
第一行是字符串 S ，第二行输入字符串 T ，保证 S 的长度大于等于 T 的长度， S 和 T 都只由小写字母组成。
```
### 输出描述

```
输出经过处理后的字符串，保证处理后的字符串不会为空串。

```

### 测试样例
#### 样例1:输入-输出-解释

```
whatthemomooofun
moo
```
```
whatthefun
```
```
无
```
### 题目来源  
`luogu.com.cn`